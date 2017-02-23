from django import forms
from rodada.models import Rodada


class Rodada_Form(forms.ModelForm):
    class Meta:
        model = Rodada
        fields = '__all__'
        widgets = {
            'duracao': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'numeroRodada':  forms.TextInput(attrs={'class': 'col-xs-6'}),
            'evento': forms.Select(attrs={'class': 'col-xs-6'})

        }
        error_messages = {
            'duracao': {'invalid': "O campo Duração deve conter um número inteiro ou decimal.",
                        'required': "O campo Duração deve ser preenchido.",
                        'max_value': "O campo Duração não deve conter um número maior que 2147483647.0.",
                        'min_value': "O campo Duração deve conter um número maior que zero.",
                        },
            'numeroRodada': {'invalid': "O campo Duração deve conter um número inteiro ou decimal.",
                    'required': "O campo Duração deve ser preenchido.",
                    'max_value': "O campo Duração não deve conter um número maior que 2147483647.0.",
                    'min_value': "O campo Duração deve conter um número maior que zero.",
                    },
            'evento': {'max_length': "O campo Evento deve conter no máximo 200 caracteres.",
                     'required': "O campo Evento deve ser preenchido.",
                     },
        }
