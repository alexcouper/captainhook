from behave import then
from nose.tools import assert_not_equal


@then('I see an error')
def step_impl(context):
    assert_not_equal('', context.last_command.err)
