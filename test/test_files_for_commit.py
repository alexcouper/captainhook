from os.path import join
import unittest

from captainhook.checkers.utils import python_files_for_commit

from . import PROJECT_DIR


class TestPythonFilesForCommit(unittest.TestCase):

    def test_recognizes_python_script(self):
        filename = join(PROJECT_DIR, 'scripts', 'captainhook')
        self.assertEquals(
            python_files_for_commit([filename]),
            [filename]
        )

    def test_recognizes_python_module(self):
        filename = join(PROJECT_DIR, 'captainhook', 'checkers', 'grep.py')
        self.assertEquals(
            python_files_for_commit([filename]),
            [filename]
        )

    def test_ignores_text_document(self):
        filename = join(PROJECT_DIR, 'README.md')
        self.assertEquals(
            python_files_for_commit([filename]),
            []
        )
