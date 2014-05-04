from django.db import models

class Foto(models.Model):
	titulo = models.CharField(max_length=50)
	url = models.CharField(max_length=255)
	ready = models.BooleanField(default=False)
