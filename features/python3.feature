Feature: pdb checker

    Background:
        Given that I am in a git repository
        And I have installed captainhook

    Scenario: When enabled, the py3 checker raises an error with non py3 syntax
        When I create a file called "py_fail.py" containing a print statment
        And I git add "py_fail.py"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
