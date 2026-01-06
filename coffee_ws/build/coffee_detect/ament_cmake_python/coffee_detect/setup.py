from setuptools import find_packages
from setuptools import setup

setup(
    name='coffee_detect',
    version='0.1.0',
    packages=find_packages(
        include=('coffee_detect', 'coffee_detect.*')),
)
