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

client_id is the Microsoft Translator API client_id, and client_secret is the Microsoft Translator API client_secret:
::

    import mstranslate

    client_id = 'XXXXXXXXXXXX'
    client_secret = 'YYYYYYYYYYYYYY'
    service_url = 'http://api.microsofttranslator.com/V2/Http.svc/Speak'

    tts_mstranslate = mstranslate.MSTranslate(client_id, client_secret, service_url, '/tmp/')
    tts_mstranslate.prepare("This is the text I will speak to you", "EN")
    output_filename = tts_mstranslate.run()

    print "Recorded TTS to %s" % output_filename


Features
--------

* Produce text to speech in different languages.


Installation
------------

Install, upgrade and uninstall python-mstranslate.py with these commands::

    $ pip install python-mstranslate
    $ pip install --upgrade python-mstranslate
    $ pip uninstall python-mstranslate


Example usage and output
------------------------

Usage:
::
    $ python-mstranslate --client_id=<client_id> --client_secret=<client_secret> -t <text> [-d <directory>] [-url <service_url>] [-h]


Example:
::
    $ mstranslate --client_id=XXXXXXXXX --client_secret=YYYYYYYYYY -t "Salut, Vous vous appelez comment?" -l fr

Output :
::
    $ Recorded TTS to /tmp/MSTRANSLATE-8895934760117809679-fr.mp3


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


TODO
--------

* replace urllib by python-request


.. _Microsoft Translate: http://www.microsoft.com/en-us/translator/translatorapi.aspx
.. _getting started with Microsoft Translator API: https://www.microsoft.com/en-us/translator/getstarted.aspx
