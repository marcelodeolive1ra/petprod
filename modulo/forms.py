from django import forms
from modulo.models import Modulo


class Modulo_Form(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'nome': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'custo_de_aquisicao': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'custo_mensal': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'tecnologia': forms.RadioSelect(attrs={'name': 'optradio', 'class': 'radio-inline'}),
            'conforto': forms.RadioSelect(attrs={'name': 'optradio', 'class': 'radio-inline'}),
            'capacidade': forms.TextInput(attrs={'class': 'col-xs-6'}),
            'preco_do_tratamento': forms.TextInput(attrs={'class': 'col-xs-6'}),
        }
        error_messages = {
            'nome': {'max_length': "O campo Nome deve conter no máximo 200 caracteres.",
                     'required': "O campo Nome deve ser preenchido.",
                     },
            'codigo': {
                'min_value': 'O campo Código deve conter um número maior que zero.',
                'invalid': 'O campo Custo de Aquisição deve conter um número inteiro ou decimal.',
                'max_value': "O campo Custo de Aquisição não deve conter um número maior que 2147483647.0.",
                'required': "O campo Custo Mensal deve ser preenchido.",
            },
            'custo_de_aquisicao': {'invalid': "O campo Custo de Aquisição deve conter um número inteiro ou decimal.",
                                   'required': "O campo Custo de Aquisição deve ser preenchido.",
                                   'max_value': "O campo Custo de Aquisição não deve conter um número maior que 2147483647.0.",
                                   'min_value': "O campo Custo de Aquisição deve conter um número maior que zero.",
                                   },
            'custo_mensal': {'invalid': "O campo Custo Mensal deve conter um número inteiro ou decimal.",
                             'required': "O campo Custo Mensal deve ser preenchido.",
                             'max_value': "O campo Custo Mensal não deve conter um número maior que 2147483647.0.",
                             'min_value': "O campo Custo Mensal deve conter um número maior que zero.",
                             },
            'capacidade': {'invalid': "O campo Capacidade deve conter um número inteiro.",
                           'required': "O campo Capacidade deve ser preenchido.",
                           'max_value': "O campo Capacidade não deve conter um número inteiro maior que 2147483647.",
                           'min_value': "O campo Capacidade deve conter um número inteiro maior que zero.",
                           },
            'preco_do_tratamento': {'invalid': "O campo Preço do Tratamento deve conter um número inteiro ou decimal.",
                                    'required': "O campo Preço do Tratamento deve ser preenchido.",
                                    'max_value': "O campo Preço do Tratamento não deve conter um número maior que 2147483647.0.",
                                    'min_value': "O campo Preço do Tratamento deve conter um número maior que zero.",
                                    },

        }