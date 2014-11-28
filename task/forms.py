from django import forms

from task.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'phone']
'''
    def clean_phone(self):
        data = self.cleaned_data['phone']
        if "1111" not in data:
            raise forms.ValidationError("Incorrect phone")
        return data

'''