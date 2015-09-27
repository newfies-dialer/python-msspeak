# python-mstranslate
Text-To-Speech with MStranslate

:Authors: Joshua Patten and Arezqui Belaid
:Description: Python wrapper for text-to-speech synthesis with Microsoft Translate

## Python Microsoft Translate Wrapper

python-mstranslate is a library to produce a text-to-speech file using [Microsoft Translate](https://msdn.microsoft.com/en-us/library/ff512420.aspx) API services.

In order to utilize this service you must sign up for Microsoft Translator service and register an application. More information on creating a Microsoft account is located at the [getting started with Microsoft Translator API](https://www.microsoft.com/en-us/translator/getstarted.aspx) page.

## Quickstart
A quick-and-dirty script to utilize the python-mstranslate library.

**APPLICATION_LOGIN** is the Microsoft Translator API client_id, and **APPLICATION_PASSWORD** is the Microsoft Translator API client_secret:
```
import mstranslate

APPLICATION_LOGIN = 'EVAL_XXXXXXX'
APPLICATION_PASSWORD = 'XXXXXXXX'
SERVICE_URL = 'http://vaas.acapela-group.com/Services/Synthesizer'

tts_mstranslate = mstranslate.MSTranslate(APPLICATION_LOGIN, APPLICATION_PASSWORD, SERVICE_URL, '/tmp/')
tts_mstranslate.prepare("This is the text I will speak to you", "EN")
output_filename = tts_mstranslate.run()

print "Recorded TTS to %s" % output_filename
```

TODO: Installation and Usage instructions
