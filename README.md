captainhook
===========

Git hook scripts

What is it
----------

This package will install a pre-commit hook for git into the
git repository that you are in at the time of installation.

Upon committing code, the pre-commit hook runs checks against the python files
to be committed and rejects the commit if any of the checks fail.


Installation
------------

Install using pip::

    pip install captainhook

Once installed into your environment, you will be able to run::

    captainhook

from within any git repo, and the pre-commit hook will be installed.

Setting Up
----------

To turn a check on or off, create a ``tox.ini`` file
in the base directory of your project with a ``captainhook`` section.

eg::


    [captainhook]
    flake8=off
    pdb=off
    python3=on


flake8, pdb and python3 checks default to being on.

Checks can also be passed arguments from the config file. This is done with
the following notation::

    <check_name>=<status>;<string to be passed through>

Currently checks can only be passed a single argument and must do the parsing
of that themselves.

flake8 obeys the configuration as per the
[flake8 docs](http://flake8.readthedocs.org/en/latest/config.html)

Checks
------

Currently supported checks are

- pdb: Checks to see if there are any uncommented
``import pdb; pdb.set_trace()`` statements in the code to be committed.

- flake8: Runs flake8 against the files that are set to be committed.

- python3: Checks to see if python files set to be committed are python3
  compatible.

Output
------

You only see output for checks that fail, otherwise silence.

Example output upon a rejected commit::


    ===============================================================================
    Checking python3
    ===============================================================================
      File "captainhook/pre_commit.py", line 77
        print 'a'
                ^
    SyntaxError: invalid syntax
    ===============================================================================
    Checking flake8
    ===============================================================================
    pre-commit.py:19:1: F401 'importlib' imported but unused
    pre-commit.py:128:1: E302 expected 2 blank lines, found 1
    setup.py:25:80: E501 line too long (89 > 79 characters)
    ===============================================================================
    Rejecting commit
    ===============================================================================


Extending
---------

You can add your own check to your git env quite easily.

Simply add a module to ``.git/hooks/checkers`` with a ``run()`` method defined.

The method should return the error string on faillure, or a False like object
on success.

For example::

    $ cat .git/hooks/checkers/mine.py
    def run():
        return "NOT A CHANCE"

This will block all commits if enabled.

A variable ``DEFAULT`` can be specified in the module and will be used to
determine the check is assumed "on" or "off". This value is only used if
tox.ini has not been used to override it.

Feedback
--------

I'm eager to get some feedback - positive or negative - about this.

Please make yourself at home, create issues if you've got problems with existing behaviour, or suggestions for future improvements or anything else.

You can reach me on twitter @couperalex.

Developing
----------

Running pre-commit.py on its own will by default cause a ``git stash`` to take
place which you probably don't want when testing a new check.

You can run the script without performing such a stash using::

    python captainhook/pre_commit.py -n
