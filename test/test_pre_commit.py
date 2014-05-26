import unittest

from mock import patch, Mock

from captainhook import pre_commit


class TestMain(unittest.TestCase):

    @patch('captainhook.pre_commit.HookConfig')
    @patch('captainhook.pre_commit.checks')
    def test_calling_run_without_args(self, checks, HookConfig):
        HookConfig().is_enabled.return_value = True
        HookConfig().arguments.return_value = ''
        testmod = Mock()
        testmod.run.return_value = None

        checks.return_value = [("testmod", testmod)]

        result = pre_commit.main()

        self.assertEquals(result, 0)
        testmod.run.assert_called_with()

    @patch('captainhook.pre_commit.HookConfig')
    @patch('captainhook.pre_commit.checks')
    def test_calling_run_with_args(self, checks, HookConfig):
        HookConfig().is_enabled.return_value = True
        HookConfig().arguments.return_value = 'yep'

        testmod = Mock()
        testmod.run.return_value = None

        checks.return_value = [("testmod", testmod)]

        result = pre_commit.main()

        self.assertEquals(result, 0)
        testmod.run.assert_called_with('yep')
