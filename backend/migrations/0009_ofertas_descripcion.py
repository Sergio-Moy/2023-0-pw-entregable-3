# Generated by Django 4.1.6 on 2023-02-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_ofertas'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertas',
            name='descripcion',
            field=models.CharField(default='vacio', max_length=500),
            preserve_default=False,
        ),
    ]