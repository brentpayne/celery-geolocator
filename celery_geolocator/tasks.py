from __future__ import absolute_import
from celery import shared_task
from celery_geolocator.config import configuration
from celery_geolocator.geocoders import GoogleRateLimitedGeocoder

__author__ = 'brent'

@shared_task
def geocode(unformatted_address):
    geocoder = GoogleRateLimitedGeocoder.getInstance()
    geocoder.initialize(daily_rate=configuration['Google']['daily_rate'], google_api_key=configuration['Google']['API_KEY'])
    return geocoder.geocode(unformatted_address)


