Feature: blocked branch checker

    Background:
        Given that I am in a git repository
        And I have installed captainhook
        And I have a tox.ini file with merge_marks=on

    Scenario: When merge marks are present the merge_marks checker raises an error when committing to master
        When I create a file in "." called "test.txt" containing some merge marks
        And I git add "test.txt"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
