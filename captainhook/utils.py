from subprocess import Popen, PIPE


class bash(object):
    "This is lower class because it is intended to be used as a method."

    def __init__(self, cmd):
        """
        TODO: Release this as a separate library!
        """
        self.p = None
        self.output = None
        self.bash(cmd)

    def bash(self, cmd):
        self.p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        self.output, self.err = self.p.communicate(input=self.output)
        return self

    def __str__(self):
        return self.output.strip().decode(encoding='UTF-8')

    def __nonzero__(self):
        return bool(str(self))


def python_files_for_commit():
    "Get all python files that are staged for commit, that are not deleted."
    files_pattern = '\.py(\..+)?$'
    return bash((
        "git diff --cached --name-status | "
        "grep -E '{files_pattern}' | "
        "grep -v -E '^D' | "
        "awk '{{ print ( $(NF) ) }}' "
    ).format(files_pattern=files_pattern))
