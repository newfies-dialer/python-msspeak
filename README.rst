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


Microsoft Speech Bing Documentation:
https://www.microsoft.com/cognitive-services/en-us/speech-api/documentation/API-Reference-REST/BingVoiceOutput


Python Bing Speech
------------------

python-msspeak is a library to synthesize text into human sounding speech
using `Microsoft Cognitive Services`_.

In order to utilize this service you must sign up for Microsoft Cognitive
service and register an application. More information on creating a Microsoft
account is located at the `getting started with Text to Speech`_ page.


Quickstart
----------

A quick-and-dirty script to utilize the python-msspeak library.

::

    from msspeak import msspeak

    subscription_key = 'XXXXXXXXXXXX'

    tts_msspeak = msspeak.MSSpeak(subscription_key, '/tmp/')
    output_filename = tts_msspeak.speak("This is the text I will speak to you", "en-US")

    print ("Recorded TTS to %s" % output_filename)


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

    $ python-msspeak --subscription_key=<subscription_key> -t <text> [-d <directory>] [-url <service_url>] [-h]

Example:
::

    $ msspeak --subscription_key=XXXXXXXXX -t "Salut, Vous vous appelez comment?" -l fr

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
Further information about Newfies-Dialer can be found at https://www.newfies-dialer.org

This module is built and supported by Star2Billing: https://www.star2billing.com


Source download
---------------

The source code is currently available on github. Fork away!

https://github.com/newfies-dialer/python-msspeak


Other libraries
---------------

* Javascript: https://github.com/nanek/mstranslator
* Python: https://pypi.python.org/pypi/mstranslator
* Python: https://github.com/bebound/Python-Microsoft-Translate-API


.. _Microsoft Cognitive Services: https://www.microsoft.com/cognitive-services/en-us/
.. _getting started with Text to Speech: https://www.microsoft.com/cognitive-services/en-us/speech-api


TODO
----

- [ ] Rename package to python-bing-speech
