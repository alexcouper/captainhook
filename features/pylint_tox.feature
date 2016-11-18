Feature: pylint obeys tox

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with pylint=on;0, flake8=off

    Scenario: When a pylint section is present in tox.ini it should be obeyed.
        When I create a file in "a" called "ignore.py" containing a line over 80 chars
        And I git add "a/ignore.py"
        And I git add "tox.ini"
        And I attempt to commit
        Then I see no errors
        And there are no uncommitted changes
