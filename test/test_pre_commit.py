import unittest

from mock import Mock, patch

from captainhook import pre_commit


class TestMain(unittest.TestCase):

    def setUp(self):
        self.get_files_patch = patch('captainhook.pre_commit.get_files')
        get_files = self.get_files_patch.start()
        get_files.return_value = ['file_one']

        self.hook_config_patch = patch('captainhook.pre_commit.HookConfig')
        self.HookConfig = self.hook_config_patch.start()
        self.HookConfig().is_enabled.return_value = True
        self.HookConfig().arguments.return_value = ''

        self.testmod = Mock()
        self.testmod.run.return_value = None
        self.checks_patch = patch('captainhook.pre_commit.checks')
        checks = self.checks_patch.start()
        checks.return_value = [("testmod", self.testmod)]

    def tearDown(self):
        self.checks_patch.stop()
        self.hook_config_patch.stop()
        self.get_files_patch.stop()

    def test_calling_run_without_args(self):
        result = pre_commit.main()

        self.assertEquals(result, 0)
        self.testmod.run.assert_called_with(['file_one'])

    def test_calling_run_with_args(self):
        self.HookConfig().arguments.return_value = 'yep'

        result = pre_commit.main()

        self.assertEquals(result, 0)
        self.testmod.run.assert_called_with(['file_one'], 'yep')
