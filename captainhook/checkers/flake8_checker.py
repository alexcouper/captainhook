# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import sys
from contextlib import contextmanager

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .utils import python_files_for_commit

DEFAULT = 'on'
CHECK_NAME = 'flake8'
NO_FLAKE_MSG = ("flake8 is required for the flake8 plugin.\n"
                "`pip install flake8` or turn it off in your tox.ini file.")


@contextmanager
def redirected(out=sys.stdout, err=sys.stderr):
    saved = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        yield
    finally:
        sys.stdout, sys.stderr = saved


def run():
    "Check flake8 errors in the code base."
    try:
        import flake8  # NOQA
    except ImportError:
        return NO_FLAKE_MSG
    from flake8.engine import get_style_guide
    from flake8.main import DEFAULT_CONFIG
    py_files = python_files_for_commit()
    if not py_files:
        return
    flake8_style = get_style_guide(config_file=DEFAULT_CONFIG, paths=['.'])
    out, err = StringIO(), StringIO()
    with redirected(out, err):
        flake8_style.check_files(py_files)
    return out.getvalue().strip()
