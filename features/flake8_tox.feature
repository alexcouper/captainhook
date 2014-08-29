Feature: flake8 obeys tox

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a flake8 section inside my tox.ini that excludes "ignore.py"

    Scenario: When a flake8 section is present in tox.ini it should be obeyed.
        When I create a file called "ignore.py" containing a line over 80 chars
        And I git add "ignore.py"
        And I git add "tox.ini"
        And I attempt to commit
        Then I see no errors
        And there are no uncommitted changes
