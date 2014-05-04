from __future__ import absolute_import

from celery import Celery


app = Celery('prueba_celery',
	broker='redis://',
	backend='redis://',
	include=['test_celery.tasks']
)

app.conf.update(
	CELERY_TASK_RESULT_EXPIRES=3600,
	CELERY_TASK_SERIALIZER='json',	# pickle, yaml, msgpack
	CELERY_RESULT_SERIALIZER='json',
	CELERY_ACCEPT_CONTENT=['json'],
	CELERY_TIMEZONE='Europe/Madrid',
	CELERY_ENABLE_UTC=True
)

if __name__ == '__main__':
	app.start()
