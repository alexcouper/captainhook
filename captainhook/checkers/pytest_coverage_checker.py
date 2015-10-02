# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import re
from .utils import bash, filter_python_files


DEFAULT = 'off'
CHECK_NAME = 'pytest-cov'
NO_PYTEST_MSG = ("pytest is required for the pytest plugin.\n"
                "`pip install pytest` or turn it off in your tox.ini file.")
NO_PYTEST_COV_MSG = ("pytest-cov is required for the pytest-cov plugin.\n"
                "`pip install pytest-cov` or turn it off in your tox.ini file.")
SCORE = 85.0


def run(files, temp_folder, arg=None):
    "Check tests coverage."
    try:
        import pytest
    except ImportError:
        return NO_PYTEST_MSG

    cmd = "pip show pytest-cov"
    if not bash(cmd).value():
        return NO_PYTEST_COV_MSG


    # set default level of threshold
    arg = arg or SCORE

    cmd = "py.test -q --cov ."
    output = bash(cmd).value()
    output = output.rstrip().splitlines()

    try:
        score = float(re.search("(\d?\d?\d)%", output[-2]).group(1))
    except:
        return "\n".join(("Something wrong with 'pytest -q --cov .' :",
                "\n".join(output),
                "Check it or disable 'pytest-cov' in your tox.ini"))
    if score >= float(arg):
        return False
    return ("Pytest-cov appreciated your tests as {0},"
        "required threshold is {1}".format(score, arg)
        )

