Feature: blocked branch checker

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with block_branch=on;master

    Scenario: When enabled on master, the block_branches checker raises an error when committing to master
        When I create a file called "test.py" containing some valid code
        And I git add "test.py"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
