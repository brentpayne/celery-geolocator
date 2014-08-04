__author__ = 'brent'

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']

CELERY_RDB_PORT='6902'

CELERY_ROUTES = {'celery_geolocator.tasks.geocode': {'queue': 'geocode', 'routing_key': 'geocode'}}

CELERY_CREATE_MISSING_QUEUES = True
