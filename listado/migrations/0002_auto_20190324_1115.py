# Generated by Django 2.1.7 on 2019-03-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='dia',
            field=models.DateField(),
        ),
    ]
