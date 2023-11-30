from django.contrib import admin
from .models import Usuario, Producto, Compras


"""class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ("email", "nombre", "nacimiento","telefono",)
    list_filter = ("email", "nombre", "nacimiento","telefono",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("nombre", "nacimiento","telefono", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password", "nombre", "nacimiento","telefono", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
admin.site.register(Usuario, CustomUserAdmin)"""
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Compras)