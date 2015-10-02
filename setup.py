#!/usr/bin/env python
# # coding: utf-8
from setuptools import find_packages, setup

long_description = open('README.md').read()

setup(
    name='captainhook',
    description='A collection of git commit hooks',
    version='0.8.6',
    long_description=long_description,
    author='Alex Couper',
    author_email='info@alexcouper.com',
    url='https://github.com/alexcouper/captainhook',
    zip_safe=False,
    scripts=[
        'scripts/captainhook'
    ],
    install_requires=[
        'docopt==0.6.1',
        'flake8',
        'isort>=4.1.1',
        'bash',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU Library or Lesser '
         'General Public License (LGPL)'),
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
