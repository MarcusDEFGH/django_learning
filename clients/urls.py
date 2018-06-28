from django.urls import path
from .views import list_clients, new_client, update_client, delete_client

urlpatterns = [
    path('list/', list_clients, name="list_clients"),
    path('new/', new_client, name="new_client"),
    path('update/<int:id>', update_client, name="update_client"),
    path('delete/<int:id>', delete_client, name="delete_client"),
]
