# Generated by Django 5.1.2 on 2024-10-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('domicilioCalle', models.CharField(max_length=100)),
                ('domicilioLocalidad', models.CharField(max_length=100)),
                ('domicilioDepartamento', models.CharField(max_length=100)),
                ('razonSocial', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]