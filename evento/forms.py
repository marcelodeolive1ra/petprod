from django import forms
from evento.models import Evento
from evento.models import Evento_ModificaEntrada


class Evento_Form(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'col-xs-12'}),

        }
        error_messages = {
            'nome': {'max_length': "O campo Nome deve conter no máximo 200 caracteres.",
                     'required': "O campo Nome deve ser preenchido.",
                     },
        }

class Evento_ModificaEntrada_Form(forms.ModelForm):
    class Meta:
        model = Evento_ModificaEntrada
        fields = ['modificadorEntrada', 'modificadorDesvio']
        widgets = {
            'modificadorEntrada': forms.TextInput(attrs={'class': 'col-xs-12'}),
            'modificadorDesvio': forms.TextInput(attrs={'class': 'col-xs-12'}),

        }

        error_messages = {
            'modificadorEntrada': {'invalid': "O campo Entrada deve conter um número inteiro ou decimal.",
                        'required': "O campo Entrada deve ser preenchido.",
                        'max_value': "O campo Entrada não deve conter um número inteiro maior que 2147483647.0.",
                        'min_value': "O campo Entrada deve conter um número inteiro maior ou igual a zero.",
                        },
            'modificadorDesvio': {'invalid': "O campo Desvio deve conter um número inteiro ou decimal.",
                        'required': "O campo Desvio deve ser preenchido.",
                        'max_value': "O campo Desvio não deve conter um número inteiro maior que 2147483647.0.",
                        'min_value': "O campo Desvio deve conter um número inteiro maior ou igual a zero.",
                        },
        }