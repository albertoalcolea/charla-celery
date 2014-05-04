from __future__ import absolute_import

from test_celery.celery import app

import time

DELAY = 5

@app.task
def add(x, y):
	time.sleep(DELAY)
	return x + y

@app.task
def mul(x, y):
	time.sleep(DELAY)
	return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def reduce(numlist):
	numbers = [item for sublist in numlist for item in sublist]
	return sum(numbers)
