from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def get_person(name):
    db = [
        {'name': 'Marcus', 'age': 22},
        {'name': 'Vinicius', 'age': 21},
        {'name': 'Maria', 'age': 20},
    ]

    for person in db:
        if person['name'] == name:
            return person
        else:
            return {'name': 'Not Found', 'age': 0}


def person(request, name):
    person = get_person(name)
    return render(request, 'person.html',
                  {'name': person['name'], 'age': person['age']})
