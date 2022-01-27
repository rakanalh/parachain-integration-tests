#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_requirements(path):
    """Read requirements, skip comments, modify git dependencies
    setup.py does not support git dependencies, so we change those to simple package names, here.
    This only leads to the correct versions in the installation because we
    always use pip to install from the requirements file before setup.py gets
    executed. Cleaner solutions wanted!
    """
    assert os.path.isfile(path), "Missing requirements file"
    ret = []
    with open(path) as requirements:
        for line in requirements.readlines():
            line = line.strip()
            if line and line[0] in ("#", "-"):
                continue
            ret.append(line)

    return ret

setup(
    name = "efinity_integration_tests",
    version = "0.0.1",
    author = "Efinity Developers",
    author_email = "info@efinity.io",
    description = ("A system for running a suite of integration tests on Efinity parachain."),
    license = "MIT",
    keywords = "efinity parachain polkadot",
    url = "http://efinity.io",
    packages=['integration', 'tests'],
    include_package_data=True,
    long_description=read('README.md'),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["integration-test = integration.main:main"]},
)
