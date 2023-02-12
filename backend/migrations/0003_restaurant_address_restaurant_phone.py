# Generated by Django 4.1.6 on 2023-02-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='Desconocido', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default='Desconocido', max_length=15),
            preserve_default=False,
        ),
    ]