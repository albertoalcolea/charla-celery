from django.urls import path

from . import views

app_name = 'filtros'
urlpatterns = [
	path('', views.index, name='index'),
	path('send/', views.send, name='send'),
]