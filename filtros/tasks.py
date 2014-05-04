from __future__ import absolute_import

from celery import shared_task

from filtros.models import Foto
from utils import imagefilter


@shared_task
def apply_filter(img_path, id):
	imagefilter.filter(img_path, img_path)
	foto = Foto.objects.get(pk=id)
	foto.ready = True
	foto.save()
