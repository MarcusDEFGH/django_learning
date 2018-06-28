from django.shortcuts import render
from .models import Client


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})
