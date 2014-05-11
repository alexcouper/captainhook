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
try:
    import ConfigParser as configparser
except ImportError:
    # python 3
    import configparser

from contextlib import contextmanager
import importlib
import os.path
import pkgutil
import sys
import types

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import checkers
from checkers.utils import bash


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
            yield name, mod


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
def gitstash(stash=True):
    """
    Validate the commit diff.

    Stash the unstaged changes first and unstash afterwards regardless of
    failure.
    """
    if stash and not changes_to_stash():
        stash = False

    if stash:
        bash("git stash -q --keep-index")
    try:
        yield
    finally:
        if stash:
            bash("git stash pop -q")


def get_hook_checks():
    """
    Return the hook check options set in tox.ini.

    Return an empty dict if none are set.
    """
    config = configparser.ConfigParser()
    if os.path.exists('tox.ini'):
        config.readfp(open('tox.ini'))
        if config.has_section('captainhook'):
            return {
                key: value for key, value in config.items('captainhook')
            }
    return {}


def main(stash):
    """
    Run the configured code checks.

    Return system exit code.
        1 - reject commit
        0 - accept commit
    """
    exit_code = 0
    hook_checks = get_hook_checks()
    with gitstash(stash):
        for name, mod in checks():

            if hook_checks.get(name, 'on') == 'on':
                errors = mod.run()

                if errors:
                    title_print("Checking {0}".format(name))
                    print(errors)
                    exit_code = 1

    if exit_code == 1:
        title_print("Rejecting commit")
    sys.exit(exit_code)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nostash', action='store_true')
    args = parser.parse_args()
    main(stash=not args.nostash)
