from behave import given, then, when
from nose.tools import assert_not_equal

from captainhook.checkers.utils import bash


@given('that I am in a git repository')
def git_init(context):
    bash('git init')


@when('I git add "{file_name}"')
def git_add(context, file_name):
    bash('git add {}'.format(file_name))


@when('I attempt to commit')
def commit(context):
    context.last_command = bash('git commit -q -m "commit"')


@then('there are uncommitted changes')
def uncommitted_changes(context):
    assert_not_equal('', bash('git status -s').output)
