# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import python_files_for_commit

DEFAULT = 'on'


def run():
    "Look for pdb.set_trace() commands in python files."
    forbidden = '^[^#"]*pdb.set_trace()'
    py_files = python_files_for_commit()
    if not py_files:
        return
    files = py_files.bash((
        "xargs grep --color --with-filename -n "
        "-e '{forbidden}'"
    ).format(
        forbidden=forbidden
    ))
    return files
