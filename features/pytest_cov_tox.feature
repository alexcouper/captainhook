Feature: pytest-cov obeys tox

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with pytest-cov=on;100


    Scenario: When a pytest-cov is present in tox.ini it should be obeyed.
       When I create a file in "." called "test_one.py" containing a line over 80 chars
        And I git add "test_one.py"
        And I git add "tox.ini"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
