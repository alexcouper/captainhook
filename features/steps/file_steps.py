from behave import when


@when('I create a file called "{file_name}" containing {contents}')
def step_create_valid_python_file(context, file_name, contents):
    with open(file_name, 'w') as f:
        if contents == 'some valid code':
            f.write("fred = 1\n")
        elif contents == 'a print statement':
            f.write("print 'x'\n")
        elif contents == 'a pdb.set_trace() statement':
            f.write("import pdb\npdb.set_trace()")
        elif contents == 'some merge marks':
            f.write("<<<<<<<\n")
        else:
            raise Exception("Unrecognised contents: {0}".format(contents))
