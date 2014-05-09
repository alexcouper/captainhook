from captainhook.utils import bash, python_files_for_commit


def flake8():
    "Check flake8 errors in the code base."
    py_files = str(python_files_for_commit())
    if not py_files:
        return
    b = bash("flake8 {0}".format(py_files.replace('\n', ' ')))
    if b.err:
        if "command not found" in b.err:
            return (
                "flake8 is required for the flake8 plugin.\n"
                "`pip install flake8` or turn it off in your tox.ini file.")
    return b
