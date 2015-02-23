# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, filter_python_files

DEFAULT = 'off'
CHECK_NAME = 'frosted'
NO_FROSTED_MSG = (
    "frosted is required for the frosted plugin.\n"
    "`pip install frosted` or turn it off in your tox.ini file.")
REQUIRED_FILES = ['tox.ini']


def run(files, temp_folder):
    "Check frosted errors in the code base."
    try:
        import frosted  # NOQA
    except ImportError:
        return NO_FROSTED_MSG

    py_files = filter_python_files(files)
    cmd = 'frosted {0}'.format(' '.join(py_files))

    return bash(cmd).value()
