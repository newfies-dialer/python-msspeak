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


default_language = "en-US"
default_gender = "Female"
default_directory = "/tmp/"


USAGE = \
    """\nUsage: msspeak --subscription_key=<subscription_key> -t <text> [-l <language>] [-g <gender>] [-d <directory>] [-h]"""


def validate_options(subscription_key, text):
    """
    Perform sanity checks on threshold values
    """
    if not subscription_key or len(subscription_key) == 0:
        print 'Error: Warning the option subscription_key should contain a string.'
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
    parser.add_option('-n', '--subscription_key', dest='subscription_key',
                      help='subscription_key for authentication')
    parser.add_option('-t', '--text', dest='text',
                      help='text to synthesize')
    parser.add_option('-l', '--language', dest='language',
                      help='language')
    parser.add_option('-g', '--gender', dest='gender',
                      help='gender')
    parser.add_option('-d', '--directory', dest='directory',
                      help='directory to store the file')
    (options, args) = parser.parse_args()
    subscription_key = options.subscription_key
    text = options.text
    language = options.language
    gender = options.gender
    directory = options.directory

    # Perform sanity checks on options
    validate_options(subscription_key, text)

    if not directory:
        directory = default_directory

    if not language:
        language = default_language

    if not gender:
        gender = default_gender

    # format = 'riff-16khz-16bit-mono-pcm'
    format = 'riff-8khz-8bit-mono-mulaw'

    # lang = 'en-AU'
    # gender = 'Female'
    tts_msspeak = MSSpeak(subscription_key, '/tmp/')
    tts_msspeak.set_cache(False)
    output_filename = tts_msspeak.speak(text, language, gender, format)

    print 'Recorded TTS to %s%s' % (directory, output_filename)


if __name__ == '__main__':
    main()
