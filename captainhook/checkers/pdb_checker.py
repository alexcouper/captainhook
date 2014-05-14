# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .grep import grep
from .utils import python_files_for_commit

DEFAULT = 'on'
CHECK_NAME = 'pdb'

forbidden = '^[^#"]*pdb.set_trace()'


def run():
    "Look for pdb.set_trace() commands in python files."
    py_files = python_files_for_commit()
    return check_files(py_files)


def check_files(filenames):
    return grep("-e '{}'".format(forbidden), ' '.join(filenames))
