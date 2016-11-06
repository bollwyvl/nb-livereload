#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from os.path import join


# should be loaded below
__version__ = None

with open(join("src", "nblivereload", "_version.py")) as version:
    exec(version.read())

with open('./README.rst') as readme:
    README = readme.read()

setup(
    name="nblivereload",
    version=__version__,
    description="Autoreload static files in the Jupyter Notebook",
    long_description=README,
    author="Nicholas Bollweg",
    author_email="nbollweg@continuum.io",
    license="BSD-3-Clause",
    url="https://github.com/bollwyvl/nb-livereload",
    keywords="ipython jupyter livereload",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License"
    ],
    package_dir={"": "src"},
    packages=["nblivereload"],
    setup_requires=["notebook", "livereload"],
    tests_require=["pytest", "requests"],
    include_package_data=True
)
