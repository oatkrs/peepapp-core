#!/usr/bin/env python

import sys

from setuptools import setup, find_packages
from pathlib import Path

if sys.version_info.major == 3 and sys.version_info.minor < 3:
    print("Unfortunately, your python version is not supported!\n Please upgrade at least to python 3.3!")
    sys.exit(1)

if sys.platform == 'darwin' or sys.platform == 'win32':
    print("Unfortunately, we do not support your platform %s" % sys.platform)
    sys.exit(1)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

install_requires = [
    'androguard==4.1.1',
    'cryptography==42.0.4',
    'dhash==1.4',
    'jellyfish==0.5.6',
    'Pillow==10.3.0',
    'requests>=2.26,<2.33',
    'six==1.15.0',
    'traitlets==4.3.2'
]

setup(
    name='peepapp_core',
    version='0.1.1',
    description='Core functionality for PeepApp',
    author='Utkarsh',
    author_email='utkarshparashar05@gmail.com',
    url='https://github.com/oatkrs/peepapp-core',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "test*", "tests"]),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)
