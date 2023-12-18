from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserModel
from .models import Avatar

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = models.InfoProd
        fields = ["titulo","cuerpo","imagen"]
        labels = {'titulo': ('Título'),'imagen': ('Imágen'),}
    def __init__(self, *args, **kwargs):
        super(EditInfoForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False

class ComprasForm(forms.ModelForm):
    class Meta:
        model = models.Compras
        fields = ["producto", "fecha_compra", "dir_envio", "provincia_envio"]
        labels = {'fecha_compra': ('Fecha de compra'), "producto": ("Producto (modelo)"), "dir_envio": ("Dirección de envío"), "provincia_envio": ("Provincia de envío"),}
        widgets = {"fecha_compra": forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'})}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]

class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        labels = {'categoria': ('Categoría'), "precio": ("Precio ($)")}

class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["producto", "categoria", "marca", "precio"]
        labels = {'categoria': ('Categoría'), "precio": ("Precio ($)")}

class InfoForm(forms.ModelForm):
    class Meta:
        model = models.InfoProd
        fields = "__all__"
        labels = {'titulo': ('Título'), "imagen": ("Imágen")}

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ["titulo", "subtitulo", "descripcion"]
        labels = {'titulo': ('Título'), 'subtitulo': ('Subtítulo'), 'descripcion': ('Descripción')}

class BlogEditForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ["titulo", "subtitulo", "descripcion"]
        labels = {'titulo': ('Título'), 'subtitulo': ('Subtítulo'), 'descripcion': ('Descripción')}
    def __init__(self, *args, **kwargs):
        super(BlogEditForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].required = False
        self.fields['subtitulo'].required = False
        self.fields['descripcion'].required = False


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
        labels = {'titulo': ('Título'), 'subtitulo': ('Subtítulo'), 'imagen': ('Imágen')}

class PostEditForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
        labels = {'titulo': ('Título'), 'subtitulo': ('Subtítulo'), 'imagen': ('Imágen')}
    def __init__(self, *args, **kwargs):
        super(PostEditForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False
        self.fields['titulo'].required = False
        self.fields['subtitulo'].required = False
        self.fields['cuerpo'].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = ["comentario"]