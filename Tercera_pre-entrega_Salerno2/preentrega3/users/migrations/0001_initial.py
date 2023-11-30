# Generated by Django 4.2.6 on 2023-11-30 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nombre', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('categoria', models.IntegerField(choices=[(1, 'Línea Blanca'), (2, 'Electrodoméstico'), (3, 'Informática')])),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('dir_envio', models.CharField(max_length=1000)),
                ('provincia_envio', models.IntegerField(choices=[(1, 'Buenos Aires'), (2, 'C.A.B.A.'), (3, 'Catamarca'), (4, 'Chaco'), (5, 'Chubut'), (6, 'Córdoba'), (7, 'Corrientes'), (8, 'Entre Ríos'), (9, 'Formosa'), (10, 'Jujuy'), (11, 'La Pampa'), (12, 'La Rioja'), (13, 'Mendoza'), (14, 'Misiones'), (15, 'Neuquén'), (16, 'Río Negro'), (17, 'Salta'), (18, 'San Juan'), (19, 'San Luis'), (20, 'Santa Cruz'), (21, 'Santa Fe'), (22, 'Santiago del Estero'), (23, 'Tierra del Fuego'), (24, 'Tucumán'), (25, 'Islas Malvinas')])),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.producto')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
