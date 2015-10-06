#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python-msspeak
----------------------------------

Tests for `python-msspeak` module.
"""

import unittest

from msspeak.command_line import main


class TestConsole(unittest.TestCase):
    def test_basic(self):
        main()
