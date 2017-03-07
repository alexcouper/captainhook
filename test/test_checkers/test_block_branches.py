# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import unittest

from mock import patch

from captainhook.checkers import block_branches


class TestMain(unittest.TestCase):

    @patch('captainhook.checkers.block_branches.bash')
    def test_run_none_blocked(self, bash):
        bash_res = bash.return_value
        bash_res.value.return_value = "master"
        with self.assertRaises(AttributeError):
            block_branches.run('something', '/tmp')

    @patch('captainhook.checkers.block_branches.bash')
    def test_run_single_blocked(self, bash):
        bash_res = bash.return_value
        bash_res.value.return_value = "master"
        retval = block_branches.run('something', '/tmp', 'master')
        self.assertEqual(retval, "Branch 'master' is blocked from being "
                                 "committed to.")

    @patch('captainhook.checkers.block_branches.bash')
    def test_run_unblocked(self, bash):
        bash_res = bash.return_value
        bash_res.value.return_value = "staging"
        retval = block_branches.run('something', '/tmp', 'master')
        self.assertIsNone(retval)

    @patch('captainhook.checkers.block_branches.bash')
    def test_run_multi_blocked(self, bash):
        bash_res = bash.return_value
        bash_res.value.return_value = "staging"
        retval = block_branches.run('something', '/tmp', 'master staging')
        self.assertEqual(retval, "Branch 'staging' is blocked from being "
                                 "committed to.")
