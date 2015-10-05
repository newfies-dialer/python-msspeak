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

from optparse import OptionParser
from mstranslate import validate_options, MSTranslate
from mstranslate import DIRECTORY, SERVICE_URL, LANGUAGE


def main():
    """
    Parse options and process text to Microsoft Translate
    """

    # Parse arguments
    parser = OptionParser()
    parser.add_option('-n', '--applogin', dest='applogin',
                      help='applicationlogin for authentication')
    parser.add_option('-p', '--password', dest='password',
                      help='Password for authentication')
    parser.add_option('-t', '--text', dest='text',
                      help='text to synthesize')
    parser.add_option('-l', '--language', dest='language',
                      help='language')
    parser.add_option('-d', '--directory', dest='directory',
                      help='directory to store the file')
    (options, args) = parser.parse_args()
    applogin = options.applogin
    password = options.password
    text = options.text
    language = options.language
    directory = options.directory

    # Perform sanity checks on options
    validate_options(applogin, password, text)

    if not directory:
        directory = DIRECTORY

    url = SERVICE_URL

    if not language:
        language = LANGUAGE

    tts_mstranslate = MSTranslate(applogin, password, url, directory)
    tts_mstranslate.set_cache(False)
    tts_mstranslate.prepare(text, language)
    output_filename = tts_mstranslate.run()

    print 'Recorded TTS to %s%s' % (directory, output_filename)


if __name__ == '__main__':
    main()
