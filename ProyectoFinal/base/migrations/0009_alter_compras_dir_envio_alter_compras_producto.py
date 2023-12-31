# Generated by Django 5.0 on 2023-12-15 04:03

import base.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_compras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='dir_envio',
            field=base.models.UpperField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='compras',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.producto'),
        ),
    ]
