from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    employee_surname = forms.CharField(validators=[validators.MinLengthValidator(1, "Please enter 1 or more characters")])
