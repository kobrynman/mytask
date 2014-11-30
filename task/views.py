import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

from task.forms import PersonForm
from task.models import Person

def person_list(request):
    person_list_all = Person.objects.all()
    context = {'person_list': person_list_all}
    return render(request, 'task/person_list.html', context)


def new_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return HttpResponseRedirect('/personlist/')
    else:
        form = PersonForm()
    context = {'form': form}
    return render(request, 'task/new_person.html', context)


def person_select(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    data = {'name': person.name, 'last_name': person.last_name, 'phone': person.phone,}
    form = PersonForm(initial=data)
    context = {'form': form, 'person': person}
    return render(request, 'task/person_select.html', context)


def update_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect('/personlist/')
    context = {'form': form, 'person': person}
    return render(request, 'task/person_select.html', context)

def delete_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.delete()
    return HttpResponseRedirect('/personlist/')


@csrf_exempt
def update_data(request):
    person_list_all = Person.objects.all()
    a = []
    for sel in person_list_all:
        temp = {"name": sel.name,"last_name": sel.last_name,"phone": sel.phone, "id": sel.id}
        a.append(temp)
    return HttpResponse(json.dumps(a, separators=(',',':')),
                        content_type="application/json"
    )

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})


@csrf_exempt
def find_by_phone(request):
    post_text = request.POST.get('phone')
    try:
        person = Person.objects.get(phone=post_text)
        my_person = {"name": person.name}
    except :
        my_person = {"name": "not found"}
    return HttpResponse(json.dumps(my_person, separators=(',',':')),
                        content_type="application/json"
    )