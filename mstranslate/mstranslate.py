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

from mstranslator import Translator
import os.path

# Package version
__version__ = '0.1'


class MSTranslate(object):

    cache = True

    def __init__(self, client_id, client_secret, directory=''):
        """construct Microsoft Translate TTS"""
        self.translator = Translator(client_id, client_secret)
        self.tts_engine = 'MSTranslator'
        self.directory = directory
        self.filename = None

    def set_cache(self, value=True):
        """
        Enable Cache of file, if files already stored return this filename
        """
        self.cache = value

    def speak(self, textstr, lang):
        """
        Run will call Microsoft Translate API and and produce audio
        """
        print("speak(textstr=%s, lang=%s)" % (textstr, lang))
        lang = lang.lower()
        concatkey = '%s-%s' % (textstr, lang)
        key = self.tts_engine + '' + str(hash(concatkey))
        self.filename = '%s-%s.wav' % (key, lang)

        # check if file exists
        fileloc = self.directory + self.filename
        if self.cache and os.path.isfile(self.directory + self.filename):
            return self.filename
        else:
            with open(fileloc, 'wb') as f:
                self.translator.speak_to_file(f, textstr, lang, format='audio/wav', best_quality=False)
                return self.filename
            return False
