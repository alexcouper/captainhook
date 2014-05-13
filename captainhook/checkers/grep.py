# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, get_files_for_commit

DEFAULT = 'off'
NO_ARG_MESSAGE = 'You must specify an argument to the grep checker.'


def run(arg=None):
    if arg is None:
        return NO_ARG_MESSAGE
    files = str(get_files_for_commit()).replace('\n', ' ')
    return bash('grep -H --exclude=tox.ini {} {}'.format(arg, files))
