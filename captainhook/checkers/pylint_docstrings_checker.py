# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import re
from .utils import bash, filter_python_files


DEFAULT = 'off'
CHECK_NAME = 'pylint_docstrings'
NO_PYLINT_MSG = ("pylint is required for the pylint_docstrings plugin.\n"
                "`pip install pylint` or turn it off in your tox.ini file.")
SCORE = 85.0


def run(files, temp_folder, arg=None):
    "Check docstring coverage of the code base."
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
    cmd = "pylint -d all -e missing-docstring {0} | grep rated".format(str_py_files)
    output = bash(cmd).value().decode('utf-8')
    output = output.split()

    if 'rated' not in output:
        return False
    score = float(re.search("(\d.\d\d)/10", output).group(1))
    if score >= float(arg):
        return False
    return ("Pylint appreciated your docstrings as {0},"
        "required threshold is {1}".format(score, arg)
        )
