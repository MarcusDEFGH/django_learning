from django.urls import path
from .views import list_clients

urlpatterns = [
    path('list/', list_clients),
]
