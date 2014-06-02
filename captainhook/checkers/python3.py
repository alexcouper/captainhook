# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, python_files_for_commit

DEFAULT = 'on'


def run():
    "Check to see if python files are py3 compatible"
    errors = []
    for py_file in python_files_for_commit():
        b = bash('2to3-2.7 {file}'.format(file=py_file))
        errors.append(b.output.decode(encoding='UTF-8'))
    return "\n".join(errors)
