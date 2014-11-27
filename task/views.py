from django.shortcuts import render, get_object_or_404
from django.http import Http404

from task.models import Person

def person_list(request):
    person_list_all = Person.objects.all()
    context = {'person_list': person_list_all}
    return render(request, 'task/person_list.html', context)


def person_select(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'task/person_select.html', {'person': person})





