from django import forms
from emprestimo.models import Emprestimo

class Emprestimo_Form(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        widgets = {
            'valor': forms.TextInput(attrs={'class': 'col-xs-6'}),
        }
        error_messages = {
            'valor': {'invalid': "O campo Valor deve conter um número inteiro ou decimal.",
                      'required': "O campo Valor deve ser preenchido.",
                      'max_value': "O campo Valor não deve conter um número inteiro maior que 2147483647.0.",
                      'min_value': "O campo Valor deve conter um número inteiro maior que zero.",
                      },
        }