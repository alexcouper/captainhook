from behave import when


@when('I create a file called "{file_name}" containing a pdb.set_trace()'
      ' statement')
def step_impl(context, file_name):
    with open(file_name, 'w') as f:
        f.write("import pdb\npdb.set_trace()")
