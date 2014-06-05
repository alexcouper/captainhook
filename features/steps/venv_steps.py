from behave import then, given
from nose.tools import assert_true, assert_false

from captainhook.checkers.utils import bash


@then('I find {package} in the current virtualenv')
def step_search_package(context, package):
    assert_true(
        bash('pip freeze | grep {0}'.format(package)).output
    )


@given(u'I don\'t have {package} in the current virtualenv')
def step_remove_package(context, package):
    bash('pip uninstall -y {0}'.format(package)).output
    assert_false(
        bash('pip freeze | grep {0}'.format(package)).output
    )
