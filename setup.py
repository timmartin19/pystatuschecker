#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = []
test_requirements = ['unittest2']

setup(
    name='py-status-checker',
    version='0.1.1',
    description="A very simple package for checking the status of a service and its components",
    author="Tim Martin",
    author_email='tim@timmartin.me',
    url='https://github.com/timmartin19/pystatuschecker',
    py_modules=['status_checker'],
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='status_checker',
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
