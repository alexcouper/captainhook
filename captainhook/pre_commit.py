#!/usr/bin/env python
# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
"""
A pre commit hook for git.

This will look at the [githooks] section of tox.ini file to see which checks
you would like to run.

To add a new check:

    1. Create a function that returns a true like, printable object for
       failure, or ``None`` for success.
    2. Add that function to ``captainhook.checkers.ALL_CHECKS``.
    3. Add a corresponding line (the name of the function) to your tox.ini file
       with 'on' (run this check) or 'off' (don't). The default behaviour is to
       run all checks defined in ``ALL_CHECKS``.
"""
from contextlib import contextmanager
import importlib
import os.path
import pkgutil
import sys
import shutil
import tempfile
import types

# We don't want pyc or __pycache__ in the checkers module.
TEMP_FOLDER = None
sys.dont_write_bytecode = True

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import checkers
from checkers.utils import bash, get_files_for_commit, HookConfig


def checks():
    """
    An iterator of valid checks that are in the installed checkers package.

    yields check name, check module
    """
    checkers_dir = os.path.dirname(checkers.__file__)
    mod_names = [name for _, name, _ in pkgutil.iter_modules([checkers_dir])]
    for name in mod_names:
        mod = importlib.import_module("checkers.{0}".format(name))

        # Does the module have a "run" function
        if isinstance(getattr(mod, 'run', None), types.FunctionType):
            # has a run method, yield it
            yield getattr(mod, 'CHECK_NAME', name), mod


def title_print(msg):
    "Pretty print a title bar."
    bar = '=' * 79
    print(bar)
    print(msg)
    print(bar)


def changes_to_stash():
    "Check there are changes to stash"
    return bool(bash('git diff'))


@contextmanager
def gitstash():
    """
    Validate the commit diff.

    Make copies of the staged changes for analysis.
    """
    global TEMP_FOLDER
    safe_directory = tempfile.mkdtemp()
    TEMP_FOLDER = safe_directory

    get_files_for_commit(copy_dest=safe_directory)

    try:
        yield
    finally:
        shutil.rmtree(safe_directory)


def main():
    """
    Run the configured code checks.

    Return system exit code.
        1 - reject commit
        0 - accept commit
    """
    global TEMP_FOLDER
    exit_code = 0
    hook_checks = HookConfig('tox.ini')
    with gitstash():
        for name, mod in checks():
            default = getattr(mod, 'DEFAULT', 'off')
            if hook_checks.is_enabled(name, default=default):
                args = hook_checks.arguments(name)
                if args:
                    errors = mod.run(args)
                else:
                    errors = mod.run()
                if errors:
                    title_print("Checking {0}".format(name))
                    print(errors.replace(TEMP_FOLDER + "/", ''))
                    exit_code = 1

    if exit_code == 1:
        title_print("Rejecting commit")
    return exit_code


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    exit_code = main()
    sys.exit(exit_code)
