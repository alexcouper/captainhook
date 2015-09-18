Feature: pytest-cov obeys tox

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with pytest-cov=on;100


    Scenario: When a pytest-cov is present in tox.ini it should be obeyed.
       When I create a file in "." called "test_foo.py" containing def test(): assert 1 == 1
        And I create a file in "." called "foo.py" containing import os; print os.listdir('.')
        And I git add "foo.py"
        And I git add "test_foo.py"
        And I git add "tox.ini"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
