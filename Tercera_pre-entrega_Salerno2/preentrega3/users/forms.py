from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from . models import Usuario, Producto, Compras


"""class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ["nombre", "email","password", "nacimiento", "telefono"]
        labels = {'telefono': ('Teléfono'),}
        widgets = {
            "nacimiento": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}),
            "password": forms.PasswordInput()
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ["nombre", "email","password", "nacimiento", "telefono"]
        labels = {'telefono': ('Teléfono'),}
        widgets = {
            "nacimiento": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}),
            "password": forms.PasswordInput()
        }"""

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["producto","categoria","marca","modelo","precio"]
 
class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ["usuario","fecha_compra","producto","dir_envio","provincia_envio"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "email", "password", "nacimiento", "telefono"]
        labels = {'telefono': ('Teléfono'),}
        widgets = {
            "nacimiento": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}),
            "password": forms.PasswordInput()
        }

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput())