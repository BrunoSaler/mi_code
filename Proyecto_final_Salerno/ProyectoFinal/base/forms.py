from django import forms
from . import models

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = models.InfoProd
        fields = ["titulo","cuerpo","imagen"]
        labels = {'titulo': ('Título'),'imagen': ('Imágen'),}