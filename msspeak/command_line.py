# -*- coding: utf-8 -*-
#
# msspeak.py - Python wrapper for text-to-speech synthesis with Microsoft Translate
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
from optparse import OptionParser
from msspeak import MSSpeak


default_language = "en"
default_directory = "/tmp/"


USAGE = \
    """\nUsage: msspeak --client_id=<client_id> --client_secret=<client_secret> -t <text> [-l <language>] [-d <directory>] [-h]"""


def validate_options(client_id, client_secret, text):
    """
    Perform sanity checks on threshold values
    """
    if not client_id or len(client_id) == 0:
        print 'Error: Warning the option client_id should contain a string.'
        print USAGE
        sys.exit(3)
    if not client_secret or len(client_secret) == 0:
        print 'Error: Warning the option client_secret should contain a string.'
        print USAGE
        sys.exit(3)
    if not text or len(text) == 0:
        print 'Error: Warning the option text should contain a string.'
        print USAGE
        sys.exit(3)


def main():
    """
    Parse options and process text to Microsoft Translate
    """

    # Parse arguments
    parser = OptionParser()
    parser.add_option('-n', '--client_id', dest='client_id',
                      help='client_id for authentication')
    parser.add_option('-s', '--client_secret', dest='client_secret',
                      help='client_secret for authentication')
    parser.add_option('-t', '--text', dest='text',
                      help='text to synthesize')
    parser.add_option('-l', '--language', dest='language',
                      help='language')
    parser.add_option('-d', '--directory', dest='directory',
                      help='directory to store the file')
    (options, args) = parser.parse_args()
    client_id = options.client_id
    client_secret = options.client_secret
    text = options.text
    language = options.language
    directory = options.directory

    # Perform sanity checks on options
    validate_options(client_id, client_secret, text)

    if not directory:
        directory = default_directory

    if not language:
        language = default_language

    tts_msspeak = MSSpeak(client_id, client_secret, directory)
    tts_msspeak.set_cache(False)
    output_filename = tts_msspeak.speak(text, language)

    print 'Recorded TTS to %s%s' % (directory, output_filename)


if __name__ == '__main__':
    main()
