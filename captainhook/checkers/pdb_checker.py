# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .grep import grep
from .utils import python_files_for_commit

DEFAULT = 'on'
CHECK_NAME = 'pdb'


def run():
    "Look for pdb.set_trace() commands in python files."
    forbidden = '^[^#"]*pdb.set_trace()'
    py_files = python_files_for_commit()
    return grep("-e '{}'".format(forbidden), ' '.join(py_files))
