import unittest
from os.path import join

from captainhook.checkers.utils import filter_python_files

from . import PROJECT_DIR


class TestPythonFiles(unittest.TestCase):

    def test_recognizes_python_script(self):
        filename = join(PROJECT_DIR, 'scripts', 'captainhook')
        self.assertEquals(
            filter_python_files([filename]),
            [filename]
        )

    def test_recognizes_python_module(self):
        filename = join(PROJECT_DIR, 'captainhook', 'checkers', 'grep.py')
        self.assertEquals(
            filter_python_files([filename]),
            [filename]
        )

    def test_ignores_text_document(self):
        filename = join(PROJECT_DIR, 'README.md')
        self.assertEquals(
            filter_python_files([filename]),
            []
        )
