import unittest

from captainhook.checkers import pdb_checker

from . import get_file


class TestPdb(unittest.TestCase):

    def test_detects_match(self):
        filename = get_file('pdb_errors.py')
        self.assertEquals(
            "{0}:1:import pdb; pdb.set_trace()".format(filename),
            pdb_checker.check_files([filename]).value()
        )

    def test_avoids_commented_out_lines(self):
        self.assertEquals(
            False,
            bool(pdb_checker.check_files([get_file('pdb_no_errors.py')]))
        )
