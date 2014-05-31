# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
try:
    import ConfigParser as configparser
except ImportError:
    # python 3
    import configparser

import os.path
from subprocess import Popen, PIPE

FILES_FOR_COMMIT = None


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

    def __unicode__(self):
        return self.value()

    def __str__(self):
        return self.value()

    def __nonzero__(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.value())

    def value(self):
        return self.output.strip().decode(encoding='UTF-8')


def get_files_for_commit(copy_dest=None):
    "Get copies of to-be-committed-files for analysis."
    global FILES_FOR_COMMIT
    if not FILES_FOR_COMMIT:
        real_files = bash(
            "git diff --cached --name-status | "
            "grep -v -E '^D' | "
            "awk '{ print ( $(NF) ) }' "
        ).value().split('\n')

        FILES_FOR_COMMIT = create_fake_copies(real_files, copy_dest)

    return FILES_FOR_COMMIT


def create_fake_copies(files, destination):
    """
    Create copies of the given list of files in the destination given.

    Creates copies of the actual files to be committed using
    git show :<filename>

    Return a list of destination files.
    """
    dest_files = []
    for filename in files:
        leaf_dest_folder = os.path.join(destination, os.path.dirname(filename))
        if not os.path.exists(leaf_dest_folder):
            os.makedirs(leaf_dest_folder)
        dest_file = os.path.join(destination, filename)
        bash("git show :{filename} > {dest_file}".format(
            filename=filename,
            dest_file=dest_file)
        )
        dest_files.append(dest_file)
    return dest_files


def python_files_for_commit(files_for_commit=None):
    "Get all python files that are staged for commit, that are not deleted."
    if not files_for_commit:
        files_for_commit = get_files_for_commit()
    return [f for f in files_for_commit
            if ('python script' in bash('file {}'.format(f)).value().lower()
                or f.endswith('.py'))]


class HookConfig(object):

    def __init__(self, config_filename):
        self.config_filename = config_filename
        self._config = {}

    def get_file(self):
        return open(self.config_filename)

    @property
    def config(self):
        if not self._config and os.path.exists(self.config_filename):
            c = configparser.ConfigParser()
            c.readfp(self.get_file())
            self._config = dict(c.items('captainhook'))
        return self._config

    def is_enabled(self, plugin, default='off'):
        setting = self.configuration(plugin)[0]
        return setting == 'on' or (setting == 'default' and default == 'on')

    def arguments(self, plugin):
        return self.configuration(plugin)[1].strip()

    def configuration(self, plugin):
        """
        Get plugin configuration.

        Return a tuple of (on|off|default, args)
        """
        conf = self.config.get(plugin, "default;").split(';')
        if len(conf) == 1:
            conf.append('')
        return tuple(conf)
