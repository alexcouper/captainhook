from behave import when, given


@when('I create a file called "{file_name}" containing a pdb.set_trace()'
      ' statement')
def step_pdb_set_trace(context, file_name):
    with open(file_name, 'w') as f:
        f.write("import pdb\npdb.set_trace()")


@when('I create a file called "{file_name}" containing a print statement')
def step_print_statement(context, file_name):
    with open(file_name, 'w') as f:
        f.write("print 'x'\n")


@given(u'I have a checker that relies on {package}')
def step_impl(context, package):
    with open(".git/hooks/checkers/dummy.py", 'w') as f:
        f.write("""
DEPENDENCIES = ['{0}']
def run():
    pass
""".format(package)
        )
