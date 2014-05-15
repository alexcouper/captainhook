# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, python_files_for_commit

DEFAULT = 'on'


def run():
    "Check to see if python files are py3 compatible"
    errors = []
    for py_file in python_files_for_commit():
        b = bash('python3 -m py_compile {0}'.format(py_file))
        if b.err:
            errors.append(b.err.decode(encoding='UTF-8'))
    return "\n".join(errors)
