import sys
from celery_geolocator.celery import app
from celery_geolocator.tasks import geocode

__author__ = 'brent'

app.config_from_object('celeryconfig')

for arg in sys.argv[1:]:
    print "geocoding", arg
    v = geocode.delay(arg)
    print v.get()