Feature: checker dependencies

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a checker that relies on isort
        And I don't have isort in the current virtualenv

    Scenario: I can install all required dependencies for checkers.
        When I run captainhook dependents
        Then I find isort in the current virtualenv
