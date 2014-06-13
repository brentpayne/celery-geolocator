from __future__ import absolute_import
from celery_geolocator.celery import app
from celery_geolocator.geocoders import GoogleRateLimitedGeocoder

__author__ = 'brent'

@app.task
def geocode(unformatted_address):
    geocoder = GoogleRateLimitedGeocoder.getInstance()
    geocoder.initialize(daily_rate=2500, google_api_key='')
    return geocoder.geocode(unformatted_address)


