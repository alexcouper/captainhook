# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import os
import sys
from contextlib import contextmanager
from os.path import join

from .utils import filter_python_files

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


DEFAULT = 'on'
CHECK_NAME = 'flake8'
NO_FLAKE_MSG = ("flake8 is required for the flake8 plugin.\n"
                "`pip install flake8` or turn it off in your tox.ini file.")
REQUIRED_FILES = ['tox.ini']


@contextmanager
def redirected(out=sys.stdout, err=sys.stderr):
    saved = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        yield
    finally:
        sys.stdout, sys.stderr = saved


def run(files, temp_folder):
    "Check flake8 errors in the code base."
    try:
        import flake8  # NOQA
    except ImportError:
        return NO_FLAKE_MSG
    from flake8.engine import get_style_guide

    py_files = filter_python_files(files)
    if not py_files:
        return
    DEFAULT_CONFIG = join(temp_folder, 'tox.ini')

    old_dir = os.curdir
    os.chdir(temp_folder)
    flake8_style = get_style_guide(config_file=DEFAULT_CONFIG)
    out, err = StringIO(), StringIO()
    with redirected(out, err):
        flake8_style.check_files(py_files)
    os.chdir(old_dir)
    return out.getvalue().strip()
