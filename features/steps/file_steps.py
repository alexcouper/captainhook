import os
import os.path

from behave import given, when


@when('I create a file in "{directory}" called "{file_name}" containing '
      '{contents}')
def step_create_valid_python_file(context, file_name, contents, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as f:
        if contents == 'some valid code':
            f.write("fred = 1\n")
        elif contents == 'a print statement':
            f.write("print 'x'\n")
        elif contents == 'a pdb.set_trace() statement':
            f.write("import pdb\npdb.set_trace()")
        elif contents == 'some merge marks':
            f.write("<<<<<<<\n")
        elif contents == 'a line over 80 chars':
            f.write('Fred = "{0}"'.format('a' * 82))
        else:
            f.write(contents)


@given('I have a flake8 section inside my tox.ini that excludes "{excludes}"')
def step_impl(context, excludes):
    with open('tox.ini', 'w') as f:
        f.write('[flake8]\n')
        f.write("exclude={0}\n".format(excludes))
        # f.write('[captainhook]\n')
