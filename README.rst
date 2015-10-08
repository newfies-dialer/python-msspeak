===============================================
MSSpeak - Microsoft Translator Speak for Python
===============================================

:Author: Arezqui Belaid and Joshua Patten
:Description: Microsoft Translator API module for Python
:Documentation: RTD https://python-msspeak.readthedocs.org
:Contributors: https://github.com/newfies-dialer/python-msspeak/graphs/contributors
:License: MIT

.. image:: https://img.shields.io/travis/newfies-dialer/python-msspeak.svg
        :target: https://travis-ci.org/newfies-dialer/python-msspeak

.. image:: https://img.shields.io/pypi/v/python-msspeak.svg
        :target: https://pypi.python.org/pypi/python-msspeak


Microsoft Translator Documentation:
http://msdn.microsoft.com/en-us/library/dd576287.aspx


Python Microsoft Speak
----------------------

python-msspeak is a library to produce a text-to-speech file using
`Microsoft Translate`_ web services.

In order to utilize this service you must sign up for Microsoft Translator
service and register an application. More information on creating a Microsoft
account is located at the `getting started with Microsoft Translator API`_ page.


Quickstart
----------

A quick-and-dirty script to utilize the python-msspeak library.

client_id is the Microsoft Translator API client_id, and client_secret is the
Microsoft Translator API client_secret:
::

    import msspeak

    client_id = 'XXXXXXXXXXXX'
    client_secret = 'YYYYYYYYYYYYYY'

    tts_msspeak = msspeak.MSSpeak(client_id, client_secret, '/tmp/')
    output_filename = tts_msspeak.speak("This is the text I will speak to you", "en")

    print "Recorded TTS to %s" % output_filename


Features
--------

* Produce text to speech in different languages.


Installation
------------

Install, upgrade and uninstall python-msspeak.py with these commands:
::

    $ pip install python-msspeak
    $ pip install --upgrade python-msspeak
    $ pip uninstall python-msspeak


Example usage and output
------------------------

Usage:
::

    $ python-msspeak --client_id=<client_id> --client_secret=<client_secret> -t <text> [-d <directory>] [-url <service_url>] [-h]

Example:
::

    $ msspeak --client_id=XXXXXXXXX --client_secret=YYYYYYYYYY -t "Salut, Vous vous appelez comment?" -l fr

Output :
::

    $ Recorded TTS to /tmp/MSTRANSLATE-8895934760117809679-fr.mp3


Feedback
--------

Feedback are more than welcome, post bugs and feature requests on github:
http://github.com/newfies-dialer/python-msspeak/issues


Extra information
-----------------

Newfies-Dialer, an open source Auto Dialer software, uses this module to
synthetize audio files being play to the end-user.
Further information about Newfies-Dialer can be found at
http://www.newfies-dialer.org

This module is built and supported by Star2Billing: http://www.star2billing.com


Source download
---------------

The source code is currently available on github. Fork away!

https://github.com/newfies-dialer/python-msspeak


API Methods
-----------

Microsoft Translator API Reference: http://msdn.microsoft.com/en-us/library/ff512404.aspx

* addTranslation (not implemented)
* addTranslationArray (not implemented)
* breakSentences (not working)
* detect (not implemented)
* detectArray (not implemented)
* getAppIdToken (not implemented) This is a legacy, replaced by
  Access Token
* getLanguageNames (not implemented)
* getLanguagesForSpeak (not implemented)
* getLanguagesForTranslate (not implemented)
* getTranslations (not implemented)
* getTranslationsArray (not implemented)
* speak: implemented
* translate (not implemented)
* translateArray (not implemented)
* translateArray2 (not implemented)


Other libraries
---------------

* Javascript: https://github.com/nanek/mstranslator
* Python: https://pypi.python.org/pypi/mstranslator
* Python: https://github.com/bebound/Python-Microsoft-Translate-API


.. _Microsoft Translate: http://www.microsoft.com/en-us/translator/translatorapi.aspx
.. _getting started with Microsoft Translator API: https://www.microsoft.com/en-us/translator/getstarted.aspx
