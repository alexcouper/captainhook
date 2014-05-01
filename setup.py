#!/usr/bin/env python
# # coding: utf-8
import os
import os.path
from setuptools import setup
PACKAGE = os.path.dirname(__file__)
long_description = open(os.path.join(PACKAGE, 'README.md')).read()

from setuptools.command.install import install


def get_git_location(folder):
    if '.git' in os.listdir(folder):
        return os.path.join(folder, '.git')
    elif folder == '/':
        return False
    else:
        return get_git_location(os.path.dirname(folder))


class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        git_location = get_git_location(os.getcwd())
        if not git_location:
            raise Exception("You need to be in a git repo to install this.")
        print "Installing to {0}".format(git_location)
        os.system("cp pre_commit.py {0}/hooks/pre-commit".format(git_location))


setup(
    name='captainhook',
    description='A collection of git commit hooks',
    long_description=long_description,
    version='0.1',
    author='Alex Couper',
    author_email='info@alexcouper.com',
    url='https://github.com/alexcouper/captainhook',
    zip_safe=True,
    package_data={
        '': ['*.txt', '*.rst', '*.md'],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
