from django import forms
from . import models


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["nombre", "email", "password", "nacimiento", "telefono"]
        labels = {'telefono': ('Teléfono'),}
        widgets = {
            "nacimiento": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}),
            "password": forms.PasswordInput()
        }

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput())
