import unittest

from mock import ANY, Mock, patch

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

        self.testmod = Mock(spec=['run'])
        self.testmod.run.return_value = None
        self.checks_patch = patch('captainhook.pre_commit.checks')
        checks = self.checks_patch.start()
        checks.return_value = [("testmod", self.testmod)]

        self.mkdtemp_patch = patch('captainhook.pre_commit.tempfile.mkdtemp')
        self.mkdtemp_patch.start().return_value = '/tmp/dir'

        self.shutil_rm_patch = patch('captainhook.pre_commit.shutil.rmtree')
        self.shutil_rm_patch.start()

    def tearDown(self):
        self.checks_patch.stop()
        self.hook_config_patch.stop()
        self.get_files_patch.stop()
        self.mkdtemp_patch.stop()
        self.shutil_rm_patch.stop()

    def test_calling_run_without_args(self):
        result = pre_commit.main()

        self.assertEquals(result, 0)
        self.testmod.run.assert_called_with(['/tmp/dir/file_one'], '/tmp/dir')

    def test_calling_run_with_args(self):
        self.HookConfig().arguments.return_value = 'yep'

        result = pre_commit.main()

        self.assertEquals(result, 0)
        self.testmod.run.assert_called_with(
            ['/tmp/dir/file_one'], '/tmp/dir', 'yep'
        )

    @patch('captainhook.pre_commit.os.path.isfile')
    @patch('captainhook.pre_commit.shutil.copy')
    def test_required_files(self, copy, isfile):
        self.testmod.REQUIRED_FILES = ['should_be_copied']
        isfile.return_value = True

        pre_commit.main()

        copy.assert_called_with('should_be_copied', ANY)

    @patch('captainhook.pre_commit.os.path.isfile')
    @patch('captainhook.pre_commit.shutil.copy')
    def test_required_files_only_copied_if_exist(self, copy, isfile):
        self.testmod.REQUIRED_FILES = ['should_be_copied']
        isfile.return_value = False

        pre_commit.main()

        self.assertEquals(0, copy.call_count)
