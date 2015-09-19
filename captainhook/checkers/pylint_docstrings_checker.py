# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .pylint_checker import *
from .utils import get_config_file


DEFAULT = 'off'
CHECK_NAME = 'pylint_docstrings'
NO_PYLINT_MSG = ("pylint is required for the {0} plugin.\n"
                "`pip install pylint` or turn it off in your {1} file.".format(CHECK_NAME, get_config_file()))
PYLINT_CMD = 'pylint -d all -e missing-docstring'
PYLINT_TARGET = 'code'
