# -*- coding: utf-8 -*-
#
# mstranslate.py - Python wrapper for text-to-speech synthesis with Microsoft Translate
# Copyright (C) 2015 Arezqui Belaid <areski@gmail.com> and Joshua Patten <joshpatten@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os.path
try:
    import simplejson as json
except ImportError:
    import json

if sys.version_info < (3, 0):
    import urllib as request
    parse = request
    import urllib2
    for method in dir(urllib2):
        setattr(request, method, getattr(urllib2, method))
    import cookielib as cookiejar
else:
    from http import cookiejar
    from urllib import parse, request

# Version Python-MSTranslate
__version__ = '0.1'

CLIENT_ID = 'XXXXXXXXXXXX'
CLIENT_SECRET = 'YYYYYYYYYYYYYY'

SERVICE_URL = 'http://api.microsofttranslator.com/V2/Http.svc/Speak'
LANGUAGE = 'en'
QUALITY = '22k'  # 22k, 8k, 8ka, 8kmu
DIRECTORY = '/tmp/'

USAGE = \
    """\nUsage: mstranslate.py -n <applicationlogin> -p <password> -t <text> [-l <language>] [-d <directory>] [-h]"""


def validate_options(applicationlogin, password, text):
    """
    Perform sanity checks on threshold values
    """
    if not applicationlogin or len(applicationlogin) == 0:
        print 'Error: Warning the option applicationlogin should contain a string.'
        print USAGE
        sys.exit(3)
    if not password or len(password) == 0:
        print 'Error: Warning the option password should contain a string.'
        print USAGE
        sys.exit(3)
    if not text or len(text) == 0:
        print 'Error: Warning the option text should contain a string.'
        print USAGE
        sys.exit(3)


class MSTranslate(object):
    # Properties
    TTS_ENGINE = None
    CLIENT_ID = None
    CLIENT_SECRET = None
    SERVICE_URL = None
    DIRECTORY = ''
    data = {}
    filename = None
    cache = True

    def __init__(self, CLIENT_ID, CLIENT_SECRET, service_url, directory=''):
        """construct Microsoft Translate TTS"""
        self.TTS_ENGINE = 'MSTRANSLATE'
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.SERVICE_URL = service_url
        self.DIRECTORY = directory

    def prepare(self, textstr, lang):
        """
        Prepare Microsoft Translate TTS
        """
        oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
        lang = lang.lower()
        concatkey = '%s-%s' % (textstr, lang)
        key = self.TTS_ENGINE + '' + str(hash(concatkey))

        self.data = {
            'language': lang,
            'format': 'audio/wav',
            'options': 'MinSize',
            'text': textstr,
        }
        self.filename = '%s-%s.wav' % (key, lang)
        # Get access token
        tokenargs = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }
        encargs = parse.urlencode(tokenargs)
        response = request.urlopen(oauth_url, encargs)
        data = json.loads(response.read())
        if "error" in data:
            print "Error retreiving access token, dumping response..."
            print data
            sys.exit(3)
        self.token = data['access_token']

    def set_cache(self, value=True):
        """
        Enable Cache of file, if files already stored return this filename
        """
        self.cache = value

    def run(self):
        """
        run will call Microsoft Translate API and and produce audio
        """

        # check if file exists
        fileloc = self.DIRECTORY + self.filename
        if self.cache and os.path.isfile(self.DIRECTORY + self.filename):
            return self.filename
        else:
            encdata = parse.urlencode(self.data)
            gettts = urllib2.build_opener()
            gettts.addheaders = [('Authorization', 'Bearer ' + self.token)]
            print self.SERVICE_URL + '/' + encdata
            ttsfile = gettts.open(self.SERVICE_URL + '?' + encdata)
            finaloutput = ttsfile.read()
            if str(finaloutput[0:4]) != "RIFF":
                print 'Error: File received was not a WAV file. Please check your credentials and try again'
                sys.exit(3)
            try:
                with open(fileloc, 'wb') as f:
                    f.write(finaloutput)
            except:
                print 'Error: Unable to write file', fileloc
                print 'Please check you have permission to write to this file.'
                sys.exit(3)
            return self.filename
