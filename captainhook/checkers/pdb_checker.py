# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import argparse

from .grep import grep
from .utils import python_files_for_commit

DEFAULT = 'on'
CHECK_NAME = 'pdb'

forbidden = '^[^#"]*pdb.set_trace()'


def run(arg=''):
    "Look for pdb.set_trace() commands in python files."
    parser = get_parser()
    args = parser.parse_args(arg.split())

    py_files = python_files_for_commit()
    if args.ignore:
        py_files = set(py_files) - set(args.ignore)
    return check_files(py_files).value()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ignore',
                        help='Ignore these files', action='append')
    return parser


def check_files(filenames):
    return grep("-e '{}'".format(forbidden), ' '.join(filenames))
