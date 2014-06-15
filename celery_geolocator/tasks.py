from __future__ import absolute_import
from celery.contrib.rdb import set_trace
from celery.signals import user_preload_options
from celery_geolocator.celery import app
from celery_geolocator.config import configuration
from celery_geolocator.geocoders import GoogleRateLimitedGeocoder

__author__ = 'brent'

@app.task
def geocode(unformatted_address):
    print 'conf', configuration
    geocoder = GoogleRateLimitedGeocoder.getInstance()
    geocoder.initialize(daily_rate=2500, google_api_key=configuration['API_KEY'])
    return geocoder.geocode(unformatted_address)


