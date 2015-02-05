from behave import given, then, when
from nose.tools import assert_equal, assert_not_equal

from captainhook.checkers.utils import bash, bash_no_errors


@given('that I am in a git repository')
def git_init(context):
    bash_no_errors('git init')
    # Travis needs this:
    bash_no_errors('git config user.email "you@example.com"')
    bash_no_errors('git config user.name "Your Name"')


@when('I git add "{file_name}"')
def git_add(context, file_name):
    bash_no_errors('git add {}'.format(file_name))


@when('I attempt to commit')
def commit(context):
    context.last_command = bash('git commit -q -m "commit"')


@then('there are uncommitted changes')
def uncommitted_changes(context):
    assert_not_equal('', bash_no_errors('git status -s').value())


@then('there are no uncommitted changes')
def no_uncommitted_changes(context):
    assert_equal(b'', bash_no_errors('git status -s').value())
