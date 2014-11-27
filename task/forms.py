from django import forms

from task.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'phone']
