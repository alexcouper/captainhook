# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .pylint_checker import *


DEFAULT = 'off'
CHECK_NAME = 'pylint_docstrings'
NO_PYLINT_MSG = ("pylint is required for the {0} plugin.\n"
                "`pip install pylint` or turn it off in your tox.ini file.".format(CHECK_NAME))
PYLINT_CMD = 'pylint -d all -e missing-docstring'
PYLINT_TARGET = 'code'
