# Generated by Django 2.1.7 on 2019-03-17 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0008_auto_20190314_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurante',
            old_name='telefono',
            new_name='telefono_restaurante',
        ),
    ]