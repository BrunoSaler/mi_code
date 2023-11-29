from django import forms

from . import models


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["nombre", "email", "password", "nacimiento", "phone"]