# Generated by Django 2.1.7 on 2019-03-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0015_auto_20190326_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='estacionamiento',
            field=models.CharField(choices=[('True', 'Si'), ('False', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='fumar',
            field=models.CharField(choices=[('True', 'Si'), ('False', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='tarjetas',
            field=models.CharField(choices=[('True', 'Si'), ('False', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='wifi',
            field=models.CharField(choices=[('True', 'Si'), ('False', 'No')], max_length=20),
        ),
    ]