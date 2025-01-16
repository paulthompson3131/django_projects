from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class MyForm(forms.Form):
    sname = forms.CharField(max_length=100, label="Employee Surname", required=False)
