from django.shortcuts import get_object_or_404, redirect, render
from .models import Client
from .forms import ClientForm


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def new_client(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_clients')
    return render(request, 'client_form.html', {'form': form})


def update_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'client_form.html', {'form': form})


def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')

    return render(request, 'client_delete.html', {'client': client})
