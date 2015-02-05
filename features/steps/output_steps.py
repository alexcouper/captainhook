from behave import then
from nose.tools import assert_equal, assert_not_equal


@then('I see an error')
def step_i_see_errors(context):
    assert_not_equal(b'', context.last_command.stderr)


@then('I see no errors')
def step_i_see_no_errors(context):
    assert_equal(b'', context.last_command.stderr)
