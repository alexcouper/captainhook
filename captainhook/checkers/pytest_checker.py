
# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, filter_python_files


DEFAULT = 'off'
CHECK_NAME = 'pytest'
NO_PYTEST_MSG = ("pytest is required for the pytest plugin.\n"
                "`pip install pytest` or turn it off in your tox.ini file.")


def run(files, temp_folder, arg=None):
    "Check tests execution."
    try:
        import pytest
    except ImportError:
        return NO_PYTEST_MSG

    cmd = "py.test -q ."
    output = bash(cmd).value()
    output = output.rstrip().splitlines()

    if 'error' in output[-1] or 'failed' in output[-1]:
        return "Py.test: {0}".format(output[-1])
