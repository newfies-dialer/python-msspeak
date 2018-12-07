# -*- coding: utf-8 -*-
import requests
import datetime
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class AccessError(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        data = response.json()
        super(AccessError, self).__init__(data["message"])


class ArgumentOutOfRangeException(Exception):
    def __init__(self, message):
        self.message = message.replace('ArgumentOutOfRangeException: ', '')
        super(ArgumentOutOfRangeException, self).__init__(self.message)


class TranslateApiException(Exception):
    def __init__(self, message, *args):
        self.message = message.replace('TranslateApiException: ', '')
        super(TranslateApiException, self).__init__(self.message, *args)


class LanguageException(Exception):
    def __init__(self, message):
        self.message = str(message)
        super(LanguageException, self).__init__(self.message)


class AccessToken(object):
    access_url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    expire_delta = datetime.timedelta(minutes=9)  # speech API valid for 10 minutes, actually

    def __init__(self, subscription_key, region = 'eastus'):
        if region != 'eastus':
            self.access_url = self.access_url.replace('eastus', region)
        self.subscription_key = subscription_key
        self._token = None
        self._expdate = None

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer " + self.token
        return r

    def request_token(self):
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        resp = requests.post(self.access_url, headers=headers)
        if resp.status_code == 200:
            self._token = resp.text
            self._expdate = datetime.datetime.now() + self.expire_delta
        else:
            raise AccessError(resp)

    @property
    def expired(self):
        return datetime.datetime.now() > self._expdate

    @property
    def token(self):
        if not self._token or self.expired:
            self.request_token()
        return self._token


class Speech(object):
    """
    Implements API for the Bing Speech service
    """
    region = 'eastus'
    api_url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"

    def __init__(self, subscription_key, region = 'eastus'):
        if region != 'eastus':
            self.api_url = self.api_url.replace('eastus', region)
        self.auth = AccessToken(subscription_key, region)

    def make_request(self, headers, data):
        resp = requests.post(self.api_url, auth=self.auth, headers=headers, data=data)
        return resp

    def speak(self, text, lang, gender, format):
        """
        Gather parameters and call.

        :param text: Text to be sent to Bing TTS API to be converted to speech
        :param lang: Language to be spoken
        :param gender: Gender of the speaker
        :param format: File format (see link below)

        Name maps and file format specifications can be found here:
        https://www.microsoft.com/cognitive-services/en-us/speech-api/documentation/api-reference-rest/bingvoiceoutput
        """

        namemap = {
            "ar-EG,Female": "Microsoft Server Speech Text to Speech Voice (ar-EG, Hoda)",
            "de-DE,Female": "Microsoft Server Speech Text to Speech Voice (de-DE, Hedda)",
            "de-DE,Male": "Microsoft Server Speech Text to Speech Voice (de-DE, Stefan, Apollo)",
            "en-AU,Female": "Microsoft Server Speech Text to Speech Voice (en-AU, Catherine)",
            "en-CA,Female": "Microsoft Server Speech Text to Speech Voice (en-CA, Linda)",
            "en-GB,Female": "Microsoft Server Speech Text to Speech Voice (en-GB, Susan, Apollo)",
            "en-GB,Male": "Microsoft Server Speech Text to Speech Voice (en-GB, George, Apollo)",
            "en-IN,Male": "Microsoft Server Speech Text to Speech Voice (en-IN, Ravi, Apollo)",
            "en-US,Male": "Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)",
            "en-US,Female": "Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)",
            "es-ES,Female": "Microsoft Server Speech Text to Speech Voice (es-ES, Laura, Apollo)",
            "es-ES,Male": "Microsoft Server Speech Text to Speech Voice (es-ES, Pablo, Apollo)",
            "es-MX,Male": "Microsoft Server Speech Text to Speech Voice (es-MX, Raul, Apollo)",
            "fr-CA,Female": "Microsoft Server Speech Text to Speech Voice (fr-CA, Caroline)",
            "fr-FR,Female": "Microsoft Server Speech Text to Speech Voice (fr-FR, Julie, Apollo)",
            "fr-FR,Male": "Microsoft Server Speech Text to Speech Voice (fr-FR, Paul, Apollo)",
            "it-IT,Male": "Microsoft Server Speech Text to Speech Voice (it-IT, Cosimo, Apollo)",
            "ja-JP,Female": "Microsoft Server Speech Text to Speech Voice (ja-JP, Ayumi, Apollo)",
            "ja-JP,Male": "Microsoft Server Speech Text to Speech Voice (ja-JP, Ichiro, Apollo)",
            "pt-BR,Male": "Microsoft Server Speech Text to Speech Voice (pt-BR, Daniel, Apollo)",
            "ru-RU,Female": "Microsoft Server Speech Text to Speech Voice (ru-RU, Irina, Apollo)",
            "ru-RU,Male": "Microsoft Server Speech Text to Speech Voice (ru-RU, Pavel, Apollo)",
            "zh-CN,Female": "Microsoft Server Speech Text to Speech Voice (zh-CN, HuihuiRUS)",
            "zh-CN,Male": "Microsoft Server Speech Text to Speech Voice (zh-CN, Kangkang, Apollo)",
            "zh-HK,Male": "Microsoft Server Speech Text to Speech Voice (zh-HK, Danny, Apollo)",
            "zh-TW,Female": "Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)",
            "zh-TW,Male": "Microsoft Server Speech Text to Speech Voice (zh-TW, Zhiwei, Apollo)",
            "nl-NL,Female": "Microsoft Server Speech Text to Speech Voice (nl-NL, HannaRUS)",
            "id-ID,Male": "Microsoft Server Speech Text to Speech Voice (id-ID, Andika)",
            "id-ID,Female": "Microsoft Server Speech Text to Speech Voice (id-ID, Andika)",
            "ar-EG,Female": "Microsoft Server Speech Text to Speech Voice (ar-EG, Hoda)",
            "hi-IN,Female": "Microsoft Server Speech Text to Speech Voice (hi-IN, Kalpana)",
            "ru-RU,Female": "Microsoft Server Speech Text to Speech Voice (ru-RU, Irina)"
        }
        if not gender:
            gender = 'Female'
        else:
            gender = gender.capitalize()

        if not lang:
            lang = 'en-US'

        if not format:
            format = 'riff-8khz-8bit-mono-mulaw'

        try:
            servicename = namemap[lang + ',' + gender]
        except (Exception):
            raise LanguageException("Invalid language/gender combination: %s, %s" % (lang, gender))

        headers = {
            "Content-type": "application/ssml+xml; charset=utf-8",
            "X-Microsoft-OutputFormat": format,
            # "X-Search-AppId": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            # "X-Search-ClientID": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
            "User-Agent": "TTSForPython"
        }

        body = "<speak version='1.0' xml:lang='%s'><voice xml:lang='%s' xml:gender='%s' name='%s'>%s</voice></speak>" % (lang, lang, gender, servicename, str(text))

        return self.make_request(headers, body)

    def speak_to_file(self, file, *args, **kwargs):
        resp = self.speak(*args, **kwargs)
        if isinstance(file, str):
            with open(file, 'wb'):
                file.write(resp.content)
        elif hasattr(file, 'write'):
            file.write(resp.content)
        else:
            raise ValueError('Expected filepath or a file-like object')


class MSSpeak(object):

    cache = True

    def __init__(self, subscription_key, directory='', region='eastus'):
        """construct Microsoft Translate TTS"""
        self.speech = Speech(subscription_key, region=region)
        self.tts_engine = 'bing_speech'
        self.directory = directory
        self.filename = None

    def set_cache(self, value=True):
        """
        Enable Cache of file, if files already stored return this filename
        """
        self.cache = value

    def speak(self, textstr, lang='en-US', gender='female', format='riff-16khz-16bit-mono-pcm'):
        """
        Run will call Microsoft Translate API and and produce audio
        """
        # print("speak(textstr=%s, lang=%s, gender=%s, format=%s)" % (textstr, lang, gender, format))
        concatkey = '%s-%s-%s-%s' % (textstr, lang.lower(), gender.lower(), format)
        key = self.tts_engine + '' + str(hash(concatkey))
        self.filename = '%s-%s.mp3' % (key, lang)

        # check if file exists
        fileloc = self.directory + self.filename
        if self.cache and os.path.isfile(self.directory + self.filename):
            return self.filename
        else:
            with open(fileloc, 'wb') as f:
                self.speech.speak_to_file(f, textstr, lang, gender, format)
                return self.filename
            return False


if __name__ == "__main__":
    subscription_key = 'XXXXXXXXXXXXXXXXXX'
    speech = Speech(subscription_key)

    # format = 'riff-16khz-16bit-mono-pcm'
    format = 'audio-16khz-64kbitrate-mono-mp3'
    lang = 'en-GB'
    gender = 'Female'
    tts_msspeak = MSSpeak(subscription_key, '/tmp/')
    output_filename = tts_msspeak.speak("Peter Piper Picked a peck of pickled peppers. Complicated words like R.N.I.B., macular degeneration, diabetes and retinitis pigmentosa could also be pronounced.", lang, gender, format)

    print ("Recorded TTS to /tmp/%s" % output_filename)
