# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import sys
from contextlib import contextmanager
from StringIO import StringIO

from flake8.engine import get_style_guide
from flake8.main import DEFAULT_CONFIG

from .utils import python_files_for_commit

DEFAULT = 'on'
CHECK_NAME = 'flake8'


@contextmanager
def redirected(out=sys.stdout, err=sys.stderr):
    saved = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        yield
    finally:
        sys.stdout, sys.stderr = saved


def run(arg=''):
    "Check flake8 errors in the code base."
    py_files = str(python_files_for_commit())
    if not py_files:
        return
    flake8_style = get_style_guide(config_file=DEFAULT_CONFIG, paths=['.'])
    out, err = StringIO(), StringIO()
    with redirected(out, err):
        flake8_style.check_files(py_files.split('\n'))
    return out.getvalue().strip()
