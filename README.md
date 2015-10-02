[![Build Status](https://travis-ci.org/alexcouper/captainhook.svg?branch=master)](https://travis-ci.org/alexcouper/captainhook)


#captainhook

Git hook scripts

## What is it

A set of configurable git hooks and checks.

Upon committing code, the pre-commit hook runs configured checks against the
files to be committed and rejects the commit if any of the checks turned on fail.

![Demo](http://f.cl.ly/items/3H0a1q2b090q2s2N3N2m/demo2.gif)

## Installation

Install using pip::

    pip install captainhook

You can then install the hooks using::

    captainhook install

from within any git repo, and the pre-commit hook will be installed.

## Running without commiting

You can perform a run against all your code base using::

    captainhook run


## Setting Up

To turn a check on or off, create a ``tox.ini`` or ``setup.cfg`` file (``tox.ini`` is used for all further examples)
in the base directory of your project with a ``captainhook`` section.

eg::


    [captainhook]
    flake8=off
    pdb=off
    python3=on
    block_branch=on;master


flake8, pdb and python3 checks default to being on.

Checks can also be passed arguments from the config file. This is done with
the following notation::

    <check_name>=<status>;<string to be passed through>

Currently checks can only be passed a single argument and must do the parsing
of that themselves.

flake8 obeys the configuration as per the
`flake8 docs <http://flake8.readthedocs.org/en/latest/config.html>`_ but any
path-related options will need to use wildcard patterns (e.g.
`exclude=*/migrations/*` instead of `exclude=migrations`).

To avoid being checked at all, you can commit using the ``--no-verify`` flag::

    git commit -a --no-verify


## Checks

Currently supported checks are

- block_branch: A branch blacklist; will reject commits if the active branch is
  in the list.

- [flake8](https://pypi.python.org/pypi/flake8): 
  Runs flake8_ on staged files (checks for [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  compliance and syntax errors).

- [pytest](http://pytest.org/latest/):
  Runs pytest_ in repository directory.

- [pytest-cov](https://pypi.python.org/pypi/pytest-cov):
  Runs pytest-cov_ in repository directory.
  You can specify level of threshold in tox.ini as number from 0 to 100.

- [pylint](http://www.pylint.org/):
  Runs pylint_ on staged files. You can specify level of threshold
  in tox.ini as number from 0 to 10.

- pylint_docstrings: Runs pylint_ to check only docstrings on staged files.
  You can specify level of threshold in tox.ini as number from 0 to 10.

- [frosted](https://pypi.python.org/pypi/frosted): 
  Runs frosted_ on staged files (checks for Python syntax errors).

- ``grep``: Runs a single ``grep`` command on staged files, rejecting the
  commit if the value being searched is found. Options are passed to ``grep``
  verbatim. Only one ``grep`` command may be specified.

- [isort](https://pypi.python.org/pypi/isort):
  Runs isort_ on staged files (checks for clean Python imports according
  to [PEP 8](https://www.python.org/dev/peps/pep-0008/) and 
  [PEP 328](https://www.python.org/dev/peps/pep-0328/)).

- merge_marks: Rejects the commit if there are any unresolved merge marks in
  staged files.

- pdb: Rejects the commit if there are any uncommented ``import pdb;
  pdb.set_trace()`` statements in staged files.

- python3: Rejects the commit if staged files are not Python 3 compatible.
  Expects ``python3`` and ``2to3-2.7`` to be in the current shell ``PATH``.

## Output

You only see output for checks that fail, otherwise silence.

Example output upon a rejected commit::


    ===============================================================================
    Checking python3
    ===============================================================================
    --- captainhook/pre_commit.py   (original)
    +++ captainhook/pre_commit.py   (refactored)
    @@ -66,7 +66,7 @@
         "Check there are changes to stash"
         return bool(bash('git diff'))

    -print 'a'
    +print('a')
    ===============================================================================
    Checking flake8
    ===============================================================================
    pre-commit.py:19:1: F401 'importlib' imported but unused
    pre-commit.py:128:1: E302 expected 2 blank lines, found 1
    setup.py:25:80: E501 line too long (89 > 79 characters)
    ===============================================================================
    Rejecting commit
    ===============================================================================


## Extending

You can add your own check to your git env quite easily.

Simply add a module to ``.git/hooks/checkers`` with a ``run()`` method defined.

The method should return the error string on faillure, or a False like object
on success.

For example::

    $ cat .git/hooks/checkers/mine.py
    DEFAULT = 'on'
    def run():
        return "NOT A CHANCE"

This will block all commits if enabled.

A checker can set the following variables:

DEFAULT: used to determine the check is assumed "on" or "off". This value is
only used if tox.ini has not been used to override it. The default DEFAULT is
off.

CHECK_NAME: To override the display name of the module.

REQUIRED_FILES: Files that, if present, should be included in the copy to the
temp directoy before analysis takes place.

## Feedback

I'm interested in hearing feedback - positive or negative - about this.

Please make yourself at home, create issues if you've got problems with existing behaviour, or suggestions for future improvements or anything else.

You can reach me on twitter @couperalex.

# Contributing

Running pre-commit.py on its own will by default create copies of the files to
be committed which you probably don't want when testing a new check.

You can run the script against all your code base using::

    python captainhook/pre_commit.py --all


## Testing

There are behavioural feature tests (based on ``behave``) found in the features
directory.

New checks should be accompanied by a corresponding behavioural test example.

To run the behavioural tests:

    $ behave

To run all other tests:

    $ nosetests

Ensure that you've installed test-requirements.txt.
