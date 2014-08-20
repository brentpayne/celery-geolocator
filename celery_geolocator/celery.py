from __future__ import absolute_import

from celery import Celery, signals
from celery.bin.base import Option
from celery_geolocator.config import configuration

__author__ = 'brent'

app = Celery('celery_geolocator',
             include=['celery_geolocator.tasks'])

app.user_options['preload'].add(
    Option('--apikey', dest="API_KEY",
           help='The API key to use in the geocoder')
)


@signals.user_preload_options.connect
def on_preload_parsed(options, **kwargs):
    configuration['Google']['API_KEY'] = options['API_KEY']
