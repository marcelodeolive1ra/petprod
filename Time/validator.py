from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms

def validate_blank(value):
    if ((' ' in value) == True):
        raise forms.ValidationError(
            ('Login não pode ter espaço em branco'),
        )