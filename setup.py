#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read().replace('.. :changelog:', '')

requirements = [
    "requests>=0.11.1,<3.0",
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-msspeak',
    version='0.4.0',
    description="Text-To-Speech with MSSpeak",
    long_description=readme + '\n\n' + changelog,
    author="Areski Belaid",
    author_email='areski@gmail.com',
    url='https://github.com/newfies-dialer/python-msspeak',
    packages=[
        'msspeak',
    ],
    package_dir={'msspeak':
                 'msspeak'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='mstranslator,tts,speech',
    entry_points={
        'console_scripts': [
            'msspeak = msspeak.command_line:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
