from django import forms
from rodada.models import Rodada


class Rodada_Form(forms.ModelForm):
    class Meta:
        model = Rodada
        fields = '__all__'
        widgets = {
            'duracao': forms.IntegerField(attrs={'class': 'col-xs-6'})
            # evento: como fazer?

        }
        error_messages = {
            'duracao': {'invalid': "O campo Duração deve conter um número inteiro ou decimal.",
                        'required': "O campo Duração deve ser preenchido.",
                        'max_value': "O campo Duração não deve conter um número maior que 2147483647.0.",
                        'min_value': "O campo Duração deve conter um número maior que zero.",
                        },
        }
