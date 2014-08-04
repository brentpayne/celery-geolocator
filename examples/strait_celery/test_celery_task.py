import sys
from celery import Celery
#from celery_geolocator.celery import app
from celery_geolocator.tasks import geocode

__author__ = 'brent'

app = Celery()
app.config_from_object('examples.strait_celery.celeryconfig')

for arg in sys.argv[1:]:
    print "geocoding", arg
    v = geocode.delay(arg)
    print v.get()
