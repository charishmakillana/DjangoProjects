import re

from django import forms
from django.core.validators import RegexValidator


def phone_number_validator():
    return RegexValidator(regex=r'^\+?1?\d{9,15}$',
                          message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        label='Enter Phone number', max_length=15, min_length=10, validators=[phone_number_validator()]
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender = forms.CheckboxInput()
    subject = forms.ChoiceField(
        choices=(
            ('Subject 1', 1),
            ('Subject 2', 2),
            ('Subject 3', 3),
        )
    )
    birthday=forms.DateField()