from django import forms
from Time.models import Time

class Time_Form(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'login': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'senha': forms.PasswordInput(attrs={'class': 'col-xs-6'}),
            'caixa': forms.TextInput(attrs={'class': 'col-xs-6'})
        ,
        }
        ''''error_messages = {
            'nome': {'invalid': "O campo Perfil deve conter um número inteiro.",
                       'required': "O campo Perfil deve ser preenchido.",
                       },
            'caixa': {'invalid': "O campo Salário deve conter um número inteiro ou decimal.",
                        'required': "O campo Salário deve ser preenchido.",
                        'min_value': "O campo Salário deve conter um número maior que zero.",
                        },
        }
'''''