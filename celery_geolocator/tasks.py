from __future__ import absolute_import
import logging
from celery import shared_task
from geopy.exc import ConfigurationError, GeocoderQueryError
from celery_geolocator.config import configuration
from celery_geolocator.geocoders import GoogleRateLimitedGeocoder, RateLimitExceededException

logger = logging.getLogger(__name__)

__author__ = 'brent'


@shared_task
def geocode(unformatted_address, geocode_type="GoogleV3", api_key=None):
    exception = False
    address, point, raw = None, None, None
    api_key = api_key if api_key else configuration['Google']['API_KEY']
    try:
        geocoder = GoogleRateLimitedGeocoder.getInstance()
        geocoder.initialize(daily_rate=configuration['Google']['daily_rate'],
                            google_api_key=api_key)
        address, point, raw = geocoder.geocode(unformatted_address)
    except RateLimitExceededException as e:
        exception = "rate limit exceeded"
    except (ConfigurationError, GeocoderQueryError, AttributeError) as e:
        logger.exception(e)
        exception = "bad query"
    except Exception as e:
        exception = str(type(e))

    return exception, address, point, raw, geocode_type
