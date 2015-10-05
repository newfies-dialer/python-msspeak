==================
Python MStranslate
==================

:Author: Arezqui Belaid and Joshua Patten
:Description: Python wrapper for text-to-speech synthesis with Microsoft Translate
:Documentation: RTD https://python-mstranslate.readthedocs.org
:Contributors: `list of contributors <https://github.com/newfies-dialer/python-mstranslate/graphs/contributors>`_
:License: MIT

.. image:: https://img.shields.io/travis/newfies-dialer/python-mstranslate.svg
        :target: https://travis-ci.org/newfies-dialer/python-mstranslate

.. image:: https://img.shields.io/pypi/v/python-mstranslate.svg
        :target: https://pypi.python.org/pypi/python-mstranslate


Text-To-Speech with MStranslate


Python Microsoft Translate Text2Speech Wrapper
----------------------------------------------

python-mstranslate is a library to produce a text-to-speech file using `Microsoft Translate`_ web services.

In order to utilize this service you must sign up for Microsoft Translator service and register an application. More information on creating a Microsoft account is located at the `getting started with Microsoft Translator API`_ page.


Quickstart
----------

A quick-and-dirty script to utilize the python-mstranslate library.

CLIENT_ID is the Microsoft Translator API client_id, and CLIENT_SECRET is the Microsoft Translator API client_secret:
::

    import mstranslate

    CLIENT_ID = 'XXXXXXXXXXXX'
    CLIENT_SECRET = 'YYYYYYYYYYYYYY'
    SERVICE_URL = 'http://api.microsofttranslator.com/V2/Http.svc/Speak'

    tts_mstranslate = mstranslate.MSTranslate(CLIENT_ID, CLIENT_SECRET, SERVICE_URL, '/tmp/')
    tts_mstranslate.prepare("This is the text I will speak to you", "EN")
    output_filename = tts_mstranslate.run()

    print "Recorded TTS to %s" % output_filename


Features
--------

* Produce text to speech in different languages.


Installation
------------

Install, upgrade and uninstall python-mstranslate.py with these commands::

  $ sudo pip install python-mstranslate
  $ sudo pip install --upgrade python-mstranslate
  $ sudo pip uninstall python-mstranslate


Example usage and output
------------------------

::

  $ Usage: python-mstranslate -applogin <applicationlogin> -p <password> -t <text> [-d <directory>] [-url <service_url>] [-h]

  $ Output : Recorded TTS to /tmp/MSTRANSLATE-8895934760117809679-EN.mp3


Feedback
--------

Feedback are more than welcome, post bugs and feature requests on github:

http://github.com/newfies-dialer/python-mstranslate/issues


Extra information
-----------------

Newfies-Dialer, an open source Auto Dialer software, uses this module to synthetize audio files being play to the end-user.
Further information about Newfies-Dialer can be found at http://www.newfies-dialer.org

This module is built and supported by Star2Billing : http://www.star2billing.com


Source download
---------------

The source code is currently available on github. Fork away!

https://github.com/newfies-dialer/python-mstranslate


Features
--------

* use python-request


.. _Microsoft Translate: http://www.microsoft.com/en-us/translator/translatorapi.aspx
.. _getting started with Microsoft Translator API: https://www.microsoft.com/en-us/translator/getstarted.aspx
