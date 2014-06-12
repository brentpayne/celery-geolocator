import sys
from celery_geolocator.tasks import geocode

__author__ = 'brent'

for arg in sys.args[1:]:
    print "geocoding", arg
    v = geocode.delay(arg)
    print v.get()