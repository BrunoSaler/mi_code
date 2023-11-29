from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from . import models


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["nombre", "email", "password", "nacimiento", "phone"]
        widgets = {
            "nacimiento": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}
            )
        }