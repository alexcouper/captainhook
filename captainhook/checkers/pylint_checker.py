# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import re
from .utils import bash, filter_python_files, get_config_file


DEFAULT = 'off'
CHECK_NAME = 'pylint'
NO_PYLINT_MSG = ("pylint is required for the {0} plugin.\n"
                "`pip install pylint` or turn it off in your {1} file.".format(CHECK_NAME, get_config_file()))
PYLINT_CMD = 'pylint'
PYLINT_TARGET = 'code'
SCORE = 85.0


def run(files, temp_folder, arg=None):
    "Check coding convention of the code base."
    try:
        import pylint
    except ImportError:
        return NO_PYLINT_MSG

    # set default level of threshold
    arg = arg or SCORE

    py_files = filter_python_files(files)
    if not py_files:
        return False

    str_py_files = " ".join(py_files)
    cmd = "{0} {1}".format(PYLINT_CMD, str_py_files)
    output = bash(cmd).value()

    if 'rated' not in output:
        return False
    score = float(re.search("(\d.\d\d)/10", output).group(1))
    if score >= float(arg):
        return False
    return ("Pylint appreciated your {0} as {1},"
        "required threshold is {2}".format(PYLINT_TARGET, score, arg)
        )
