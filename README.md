celery-geolocator
=================

Celery worker that wraps and rate limits calls to geolocators.  It uses geopy for calling geolocation APIs.

© Celery-GeoLocator Project and individual contributors under the
[MIT License](https://github.com/geopy/geopy/blob/master/LICENSE).


### Install requirements

This package requires that you already have celery installed, see [celery install instruction](http://www.celeryproject.org/install/), and an appropriate broker setup, [celery brokers](http://docs.celeryproject.org/en/latest/getting-started/brokers/index.html).


### Run geocoder celery worker

We only want to use our free daily Google API limit of geocode requests per day.  To help maintain this, we
use a single celery worker that runs a rate limited geocoder.  The celery worker reads all tasks off a queue
populated by python calls to **`geocode.delay(unformatted_address)`**.  running the celery worker.

This example assumes rabbitmq is setup on localhost using default ports.

```sh
$ celery worker --app celery_geolocator --loglevel=info -Q geocode --config=examples.strait_celery.celeryconfig --apikey=<GOOGLE_API_KEY>
$ python examples/strait_celery/test_celery_task.py "Bourbon County"
   > geocoding Bourbon County
   > [u'Bourbon County, KY, USA', [38.2170752, -84.2278796]]
```

#### NOTE: DO NOT DO THIS:
```sh
$ celery worker --app celery_geolocator -Q=geocode ...
```
It will set the worker to listen to a queue named `=geocode`.  Never use the *-Q* option with an *=*.


### Roadmap

 * Incorporate yaml or json configuration files for setting celery_geolocator configuration options
 * Add options for using other geocoders than Google, expose more geopy features, etc.
