#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path, listdir


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def files(dirname):
    return [path.join(dirname, filename) for filename in listdir(dirname)]


setup(
    name="alto-nova",
    version="0.1",
    description="A cli wrapper for nova",
    url="https://github.com/openalto/alto-nova",
    author="Kai Gao, Jensen Zhang",
    author_email="emiapwil@gmail.com, hack@jensen-zhang.site",
    classifiers=[
        "License :: OSI Approved :: Academic Free License 3.0",
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intented Audience :: Developers",
        "Topic :: Network :: Tools",
    ],
    license="MIT",
    long_description=read("README.rst"),
    packages=find_packages(),
    scripts=files('bin'),
    zip_safe=False
)
