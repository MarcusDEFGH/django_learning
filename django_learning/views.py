from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello')


def articles(request, year):
    return HttpResponse('And the year was {}...'.format(year))


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
            return 'Name not found'


def person(request, name):
    person = get_person(name)
    return HttpResponse('Person found! \
                        Name: {} Age: {}'.format(
                        person['name'], person['age']))
