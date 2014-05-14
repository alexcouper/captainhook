try:
    import StringIO as io
except ImportError:
    # Python3
    import io

import unittest

from captainhook.checkers.utils import HookConfig


class TestHookConfig(unittest.TestCase):

    def test_get_hook_configuration(self):
        h = HookConfig('tox.ini')
        conf = ("[captainhook]\n"
                "pdb:off\n"
                "flake8:on\n"
                "python3:on")
        h.get_file = lambda: io.StringIO(conf)

        self.assertEquals(h.configuration('flake8'), ('on', ''))
        self.assertEquals(h.configuration('pdb'), ('off', ''))

    def test_hooks_enabled(self):
        h = HookConfig('tox.ini')
        conf = ("[captainhook]\n"
                "flake8:on\n"
                "python3:on")
        h.get_file = lambda: io.StringIO(conf)

        self.assertTrue(h.is_enabled('flake8'))
        self.assertFalse(h.is_enabled('somethingelse'))

        # Test defaults
        self.assertTrue(h.is_enabled('somethingelse', default='on'))
        self.assertTrue(h.is_enabled('flake8', default='off'))

    def test_extra_arguments(self):
        h = HookConfig('tox.ini')
        conf = ("[captainhook]\n"
                "flake8:on; --show-source\n"
                "python3:on")
        h.get_file = lambda: io.StringIO(conf)

        self.assertEquals('--show-source', h.arguments('flake8'))
        self.assertTrue(h.is_enabled('flake8'))
