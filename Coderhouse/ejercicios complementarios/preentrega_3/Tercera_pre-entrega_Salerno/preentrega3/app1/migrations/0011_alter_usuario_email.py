# Generated by Django 4.2.6 on 2023-11-30 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_phone_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
