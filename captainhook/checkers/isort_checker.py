# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, filter_python_files

DEFAULT = 'off'
CHECK_NAME = 'isort'
NO_ISORT_MSG = ("isort is required for the flake8 plugin.\n"
                "`pip install isort` or turn it off in your tox.ini file.")
REQUIRED_FILES = ['.editorconfig', '.isort.cfg', 'setup.cfg']


def run(files, temp_folder):
    "Check flake8 errors in the code base."
    try:
        import isort  # NOQA
    except ImportError:
        return NO_ISORT_MSG

    py_files = filter_python_files(files)

    return bash('isort -df {0}'.format(' '.join(py_files))).value()
