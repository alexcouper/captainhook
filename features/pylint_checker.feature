Feature: pylint checker

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with pylint=on

    Scenario: When pylint are present the pylint checker raises an error when committing
        When I create a file in "a" called "ignore.py" containing a line over 80 chars
        And I git add "a/ignore.py"
        And I git add "tox.ini"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
