from django.conf.urls import url

from filtros import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^send/$', views.send, name='send'),
]