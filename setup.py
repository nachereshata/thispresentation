#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='thispresentation',
    version='0.0.1',
    description='A gentle introduction to packaging',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/maxhumber/thispresentation',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['thispresentation'],
    zip_safe=False,
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
