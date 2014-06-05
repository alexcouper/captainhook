from behave import given, when

from captainhook.checkers.utils import bash


@given('I have installed captainhook')
def step_impl(context):
    bash('captainhook install')


@when('I run captainhook dependents')
def step_dependents(context):
    bash('captainhook dependents')
