# Generated by Django 4.1.6 on 2023-02-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[(1, 'Activo'), (2, 'Inactivo')], max_length=1)),
                ('restaurantes', models.CharField(choices=[(1, 'Sabor y punto'), (2, 'Corralito'), (3, 'Sabores y mixturas')], max_length=1)),
            ],
        ),
    ]