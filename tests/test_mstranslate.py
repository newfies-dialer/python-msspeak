#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python-mstranslate
----------------------------------

Tests for `python-mstranslate` module.
"""

import unittest

from mstranslate.command_line import main


class TestConsole(unittest.TestCase):
    def test_basic(self):
        main()
