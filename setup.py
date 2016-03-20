#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-collapse-whitespace-templatetag',

    url="https://chris-lamb.co.uk/projects/django-collapse-whitespace-templatetag",
    version='1.0.2',
    description="Simple template tag for Django to collapse whitespace",

    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license="BSD",

    packages=find_packages(),
    include_package_data=True,

    install_requires=(
        'Django>=1.8',
    ),
)
