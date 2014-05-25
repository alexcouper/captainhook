#coding: utf-8

import unittest

from captainhook.checkers import utils

from . import get_file


class TestBash(unittest.TestCase):

    def test_handles_non_ascii_output(self):
        b = utils.bash("echo ðæ")
        self.assertTrue(bool(b))

