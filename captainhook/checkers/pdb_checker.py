# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import argparse

from .grep import grep
from .utils import filter_python_files

DEFAULT = 'on'
CHECK_NAME = 'pdb'

forbidden = '^[^#"]*pdb.set_trace()'


def run(files, temp_folder, arg=''):
    "Look for pdb.set_trace() commands in python files."
    parser = get_parser()
    args = parser.parse_args(arg.split())

    py_files = filter_python_files(files)
    if args.ignore:
        orig_file_list = original_files(py_files, temp_folder)
        py_files = set(orig_file_list) - set(args.ignore)
        py_files = [temp_folder + f for f in py_files]

    return check_files(py_files).value()


def original_files(destination_files, destination):
    """
    Return a list of original filenames from the list given.
    """
    return [f.replace(destination + '/', '') for f in destination_files]


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ignore',
                        help='Ignore these files', action='append')
    return parser


def check_files(filenames):
    return grep("-e '{}'".format(forbidden), ' '.join(filenames))
