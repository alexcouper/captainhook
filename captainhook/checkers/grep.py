# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, get_files_for_commit

DEFAULT = 'off'
NO_ARG_MESSAGE = 'You must specify an argument to the grep checker.'


def grep(args, files):
    return bash('grep -n -H --exclude=tox.ini {} {}'.format(args, files))


def run(arg=None):
    if arg is None:
        return NO_ARG_MESSAGE
    files = ' '.join(get_files_for_commit())
    return grep(arg, files).value()
