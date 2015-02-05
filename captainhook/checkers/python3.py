# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, filter_python_files

DEFAULT = 'on'


def run(files, temp_folder):
    "Check to see if python files are py3 compatible"
    errors = []
    for py_file in filter_python_files(files):
        # We only want to show errors if we CAN'T compile to py3.
        # but we want to show all the errors at once.
        b = bash('python3 -m py_compile {0}'.format(py_file))
        if b.stderr:
            b = bash('2to3-2.7 {file}'.format(file=py_file))
            errors.append(b.value())
    return "\n".join(errors)
