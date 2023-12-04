from django import forms
from . import models

category=(
    (1, 'Línea Blanca'),
    (2, 'Electrodoméstico'),
    (3, 'Informática'),
)

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
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput())

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        labels = {'categoria': ('Categoría'), "precio": ("Precio ($)"),}

class ComprasForm(forms.ModelForm):
    class Meta:
        model = models.Compras
        fields = "__all__"
        labels = {'fecha_compra': ('Fecha de compra'), "producto": ("Producto (modelo)"), "dir_envio": ("Dirección de envío"), "provincia_envio": ("Provincia de envío"),}

class ProductoBuscarForm(forms.Form):
    producto = forms.CharField()

class Test1Form(forms.Form):
    producto = forms.ChoiceField(choices=category)