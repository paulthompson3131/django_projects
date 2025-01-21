from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class MyForm(forms.Form):
    sname = forms.CharField(max_length=100, label="Employee Surname", required=False)

class NumberOfPeopleForm(forms.Form):
    number_of_people = forms.IntegerField(label="Number of Employees (Between 1 and 100)", required=False, min_value = 1, max_value=100, initial=10)

    def clean_number_of_people(self):
        if self.cleaned_data.get('number_of_people'):
            try:
                return int(self.cleaned_data['number_of_people'])
            except ValueError:
                raise ValidationError("Invalid number")
        return 0
