from behave import given

from captainhook.checkers.utils import bash_no_errors


@given('I have installed captainhook')
def step_impl(context):
    bash_no_errors('captainhook install')
