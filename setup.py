#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'matplotlib',# TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='core',
    version='0.1.0',
    description="An open source core library to help abstract the basic parts of numpy and scipy for beginners. Edit",
    long_description=readme + '\n\n' + history,
    author="Olamilekan Wahab",
    author_email='olamyy53@gmail.com',
    url='https://github.com/Olamyy/core',
    packages=[
        'core',
    ],
    package_dir={'core':
                 'core'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='core',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
