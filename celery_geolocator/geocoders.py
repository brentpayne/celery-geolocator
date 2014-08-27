from datetime import timedelta
import sys
from geopy.exc import GeocoderQueryError, GeocoderQuotaExceeded, ConfigurationError

from geopy.geocoders import GoogleV3

from celery_geolocator.decorators import rate_limit, MaxCallsExceededException
from celery_geolocator.singleton import Singleton


__author__ = 'brent'


class RateLimitExceededException(MaxCallsExceededException):
    def __init__(self, number, timedelta, *args, **kwargs):
        super(RateLimitExceededException, self).__init__(*args, **kwargs)
        self.number = number
        self.timedelta = timedelta


class GoogleRateLimitedGeocoder(Singleton):
    def __init__(self):
        self.uninitialized = False

    def initialize(self, daily_rate=2500, google_api_key=None):
        self.daily_rate = daily_rate
        self.timedelta = timedelta(days=1)
        self.between_timedelta = timedelta(seconds=1)
        google_api_key = google_api_key
        if google_api_key:
            self.geolocator = GoogleV3(api_key=google_api_key)
        else:
            self.geolocator = GoogleV3()
        self.initialized = True

    def geocode(self, unformatted_address):
        @rate_limit(one_per_timedelta=self.between_timedelta,
                    max_limit=self.daily_rate,
                    refresh_after_timedelta=self.timedelta)
        def rate_limited_geocoding(unformatted_address):
            location = self.geolocator.geocode(unformatted_address)
            return location.address, (location.latitude, location.longitude, location.altitude), location.raw

        try:
            return rate_limited_geocoding(unformatted_address)
        except (MaxCallsExceededException, GeocoderQuotaExceeded) as _:  # noqa
            #reraise more explicit exception with same traceback
            description = 'We exceeded our daily limit for Google Geocoding API'
            trace = sys.exc_info()[2]
            raise RateLimitExceededException(self.daily_rate, self.timedelta, description), None, trace
        except (ConfigurationError, GeocoderQueryError, AttributeError):
            raise