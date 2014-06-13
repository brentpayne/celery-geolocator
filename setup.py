#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


requirements = [
    'celery==3.1.11',
]


setup(
    name='celery_geolocator',
    version='0.0.1',
    description='KennyG SAX Handler',
    long_description="A developer friendly library for writing SAX XML parsers.",
    author='Brent Payne',
    author_email='brent.payne@gmail.com',
    url='http://www.github.com/brentpayne/celery-geolocator',
    packages=find_packages(),
    install_requires=requirements,
    keywords=['celery', 'geopy', 'geolocate', 'celery-geolocator', 'geolocator'],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ], requires=['celery']

)
