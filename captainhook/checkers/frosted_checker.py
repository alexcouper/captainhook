# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, filter_python_files, get_config_file

DEFAULT = 'off'
CHECK_NAME = 'frosted'
NO_FROSTED_MSG = (
    "frosted is required for the frosted plugin.\n"
    "`pip install frosted` or turn it off in your {} file.".format(get_config_file()))
REQUIRED_FILES = [get_config_file()]


def run(files, temp_folder):
    "Check frosted errors in the code base."
    try:
        import frosted  # NOQA
    except ImportError:
        return NO_FROSTED_MSG

    py_files = filter_python_files(files)
    cmd = 'frosted {0}'.format(' '.join(py_files))

    return bash(cmd).value()
