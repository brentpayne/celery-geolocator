#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


requirements = [
    'celery>=3.1',
    'geopy>=1.1'
]


setup(
    name='celery_geolocator',
    version='0.0.2',
    description='Celery Geolocator',
    long_description="A celery wrapper around geopy",
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
    ], requires=['celery', 'geopy']

)
