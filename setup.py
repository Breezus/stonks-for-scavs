# -*- coding: utf-8 -*
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='scavstonks',
    version='0.1.0',
    description='Creating data and numbers for all of the scavs',
    long_description=readme,
    author='mattbrockman',
    author_email='mattbrockman95@gmail.com',
    packages=find_packages(exclude=('tests'))
)
