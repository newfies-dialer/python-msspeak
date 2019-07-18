import requests
import os

if 'SPEECH_SERVICE_KEY' in os.environ:
    subscription_key = os.environ['SPEECH_SERVICE_KEY']
else:
    print('Environment variable for your subscription key is not set.')
    exit()


def get_token(subscription_key):
    fetch_token_url = 'https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    print(access_token)
    return access_token


if __name__ == '__main__':

    access_token = get_token(subscription_key)

    headers = {
        'Authorization': 'Bearer ' + access_token,
        # 'Content-Type': 'application/ssml+xml',
    }

    voice_url = 'https://eastus.tts.speech.microsoft.com/cognitiveservices/voices/list'
    response = requests.get(voice_url, headers=headers)
    # import ipdb; ipdb.set_trace()
    # json_content = response.content
    print(response.content)

