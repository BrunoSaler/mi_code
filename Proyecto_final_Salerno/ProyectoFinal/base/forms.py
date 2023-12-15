from django import forms
from . import models

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = models.InfoProd
        fields = ["titulo","cuerpo","imagen"]
        labels = {'titulo': ('Título'),'imagen': ('Imágen'),}

class ComprasForm(forms.ModelForm):
    class Meta:
        model = models.Compras
        fields = ["producto", "fecha_compra", "dir_envio", "provincia_envio"]
        labels = {'fecha_compra': ('Fecha de compra'), "producto": ("Producto (modelo)"), "dir_envio": ("Dirección de envío"), "provincia_envio": ("Provincia de envío"),}
        widgets = {"fecha_compra": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'})}