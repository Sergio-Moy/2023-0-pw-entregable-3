# Generated by Django 4.1.6 on 2023-02-12 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_merge_20230211_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('restaurante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.restaurant')),
            ],
        ),
    ]