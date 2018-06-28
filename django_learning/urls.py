from django.contrib import admin
from django.urls import path, include
from .views import hello, person
from django.conf import settings
from django.conf.urls.static import static
from clients import urls as clients_urls

urlpatterns = [
    path('hello/', hello),
    path('person/<str:name>/', person),
    path('admin/', admin.site.urls),
    path('client/', include(clients_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #TODO: remove
