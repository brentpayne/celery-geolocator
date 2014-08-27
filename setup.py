#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


requirements = [
    'celery>=3.1.11',
    'geopy>=0.99'
]


setup(
    name='celery_geolocator',
    version='0.0.10',
    description='Celery Geolocator',
    long_description="A celery wrapper around geopy",
    author='Brent Payne',
    author_email='brent.payne@gmail.com',
    url='http://www.github.com/brentpayne/celery-geolocator',
    packages=[
        'celery_geolocator',
    ],
    install_requires=requirements,
    keywords=['celery', 'geopy', 'geolocate', 'celery-geolocator', 'geolocator', 'celery_geolocator'],
    classifiers=[
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Lesser General Public License v3" +
         " (LGPLv3)")
    ], requires=['celery', 'geopy']

)
