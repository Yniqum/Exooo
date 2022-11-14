"""A setuptools base setup module
"""
from os import path
from setuptools import setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='My_package',
    version='1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gite.Yniqum',
    author='Dmitry',
    author_email='yniqum@gmail.com',
    package_dir={'': 'My_package'},
    packages=find_namespace_packages(where='My_package'),
    python_requires='>=3.9',
    install_requires=['prettytable'],
)
