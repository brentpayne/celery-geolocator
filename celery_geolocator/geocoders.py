from datetime import timedelta
from geopy.geocoders import GoogleV3
from celery_geolocator.lib.decorators import rate_limit
from celery_geolocator.lib.singleton import Singleton

__author__ = 'brent'


class GoogleRateLimitedGeocoder(Singleton):
    def __init__(self):
        self.uninitialized = False

    def initialize(self, daily_rate=2500, google_api_key=None):
        self.daily_rate = daily_rate
        google_api_key = google_api_key
        if(google_api_key):
            self.geolocator = GoogleV3(api_key=google_api_key)
        else:
            self.geolocator = GoogleV3()
        self.initialized = True

    def geocode(self, unformatted_address):
        @rate_limit(one_per_timedelta=timedelta(seconds=1), max_limit=self.daily_rate, refresh_after_timedelta=timedelta(days=1))
        def rate_limited_geocoding(unformatted_address):
            canonical_address, (latitude, longitude) = self.geolocator.geocode(unformatted_address)
            return canonical_address, (latitude, longitude)
        return rate_limited_geocoding(unformatted_address)
