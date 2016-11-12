from django import forms
from area.models import Area


class Area_Form(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'col-xs-6'}),

        }
        error_messages = {
            'nome': {'max_length': "O campo Nome deve conter no máximo 200 caracteres.",
                     'required': "O campo Nome deve ser preenchido.",
                     },
        }