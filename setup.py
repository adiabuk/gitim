#!/usr/bin/env python

"""
Setup script for gitim
"""

from setuptools import setup
from gitim import (__version__ as VERSION, __author__ as AUTHOR,
                   __name__ as NAME, __license__ as LICENSE)

if __name__ == '__main__':

    with open('requirements.txt') as reqs_file:
        REQS = reqs_file.readlines()

    setup(
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        license=LICENSE,
        install_requires=REQS,
        entry_points={'console_scripts':['gitim=gitim:main']},
        py_modules=[NAME]
    )
