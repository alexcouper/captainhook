from behave import given

from captainhook.checkers.utils import bash


@given('I have installed captainhook')
def step_impl(context):
    bash('captainhook')
