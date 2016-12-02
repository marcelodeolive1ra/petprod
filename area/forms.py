from django import forms
from area.models import Area
from area.models import Area_ClasseSocial

class Area_Form(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'col-xs-12'}),

        }
        error_messages = {
            'nome': {'max_length': "O campo Nome deve conter no máximo 200 caracteres.",
                     'required': "O campo Nome deve ser preenchido.",
                     },
        }

class Area_ClasseSocial_Form(forms.ModelForm):
    class Meta:
        model = Area_ClasseSocial
        fields = ['entrada','desvios']
        widgets = {
            'entrada': forms.TextInput(attrs={'class': 'col-xs-12'}),
            'desvios': forms.TextInput(attrs={'class': 'col-xs-12'}),

        }
        error_messages = {
            'entrada': {'invalid': "O campo Entrada deve conter um número inteiro ou decimal.",
                      'required': "O campo Entrada deve ser preenchido.",
                      'max_value': "O campo Entrada não deve conter um número inteiro maior que 2147483647.0.",
                      'min_value': "O campo Entrada deve conter um número inteiro maior ou igual a zero.",
                      },
            'desvios': {'invalid': "O campo Desvio deve conter um número inteiro ou decimal.",
                        'required': "O campo Desvio deve ser preenchido.",
                        'max_value': "O campo Desvio não deve conter um número inteiro maior que 2147483647.0.",
                        'min_value': "O campo Desvio deve conter um número inteiro maior ou igual a zero.",
                        },
        }