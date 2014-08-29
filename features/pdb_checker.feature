Feature: pdb checker

    Background:
        Given that I am in a git repository
        And I have installed captainhook

    Scenario: When enabled, the pdb checker raises an error with pdb statements
        When I create a file in "." called "pdb_fail.py" containing a pdb.set_trace() statement
        And I git add "pdb_fail.py"
        And I attempt to commit
        Then I see an error
        And there are uncommitted changes
