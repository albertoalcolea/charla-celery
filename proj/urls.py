from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('filtros.urls', namespace='filtros')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)