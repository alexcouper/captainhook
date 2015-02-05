# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import argparse

from .utils import bash

CHECK_NAME = 'block_branch'


def run(files, temp_folder, arg=None):
    "Check we're not committing to a blocked branch"
    parser = get_parser()
    argos = parser.parse_args(arg.split())

    current_branch = bash('git symbolic-ref HEAD').value().decode('utf-8')
    current_branch = current_branch.replace('refs/heads/', '').strip()
    if current_branch in argos.branches:
        return ("Branch '{0}' is blocked from being "
                "committed to.".format(current_branch))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('branches', metavar='B', nargs='+',
                        help='a branch to block commits to')
    return parser
