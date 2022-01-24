#!/usr/bin/env python

from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import find_packages, setup

setup_args = generate_distutils_setup(
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

setup(**setup_args)
