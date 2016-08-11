from django import forms
from classe_social.models import Classe_Social


class Classe_Social_Form(forms.ModelForm):
    class Meta:
        model = Classe_Social
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'preco_atendimento': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'nivel_especialidade': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'nivel_tecnologia': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'media_conforto': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'velocidade_atendimento': forms.TextInput(attrs={'class': 'col-xs-6'}),
        }
        error_messages = {
            'nome': {'max_length': "O campo Nome deve conter no máximo 200 caracteres.",
                     'required': "O campo Nome deve ser preenchido.",
                     },
            'preco_atendimento': {
                'min_value': 'O campo Preço de atendimento deve conter um número maior que zero.',
                'invalid': 'O campo Preço de atendimento deve conter um número inteiro ou decimal.',
                'max_value': "O campo Preço de atendimento não deve conter um número maior que 3.0.",
                'required': "O campo Preço de atendimento deve ser preenchido.",
            },
            'nivel_especialidade': {'invalid': "O campo Nível de Especialidade deve conter um número inteiro ou decimal.",
                                   'required': "O campo Nível de Especialidade deve ser preenchido.",
                                   'max_value': "O campo Nível de Especialidade não deve conter um número maior que 3.0.",
                                   'min_value': "O campo Nível de Especialidade deve conter um número maior que zero.",
                                   },
            'nivel_tecnologia': {'invalid': "O campo Nível de tecnologia deve conter um número inteiro ou decimal.",
                             'required': "O campo Nível de tecnologia deve ser preenchido.",
                             'max_value': "O campo Nível de tecnologia não deve conter um número maior que 3.0.",
                             'min_value': "O campo Nível de tecnologia deve conter um número maior que zero.",
                             },
            'media_conforto': {'invalid': "O campo Media de conforto deve conter um número inteiro ou decimal.",
                           'required': "O campo Media de conforto deve ser preenchido.",
                           'max_value': "O campo Media de conforto não deve conter um número inteiro maior que 3.0.",
                           'min_value': "O campo Media de conforto deve conter um número inteiro maior que zero.",
                           },
            'velocidade_atendimento': {'invalid': "O campo Velocidade de atendimento deve conter um número inteiro ou decimal.",
                                    'required': "O campo Velocidade de atendimento deve ser preenchido.",
                                    'max_value': "O campo Velocidade de atendimento não deve conter um número maior que 3.0.",
                                    'min_value': "O campo Velocidade de atendimento deve conter um número maior que zero.",
                                    },

        }