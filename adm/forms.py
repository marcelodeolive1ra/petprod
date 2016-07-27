from django import forms

class FormularioDeLogin(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()