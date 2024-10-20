# Generated by Django 5.1.2 on 2024-10-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('unidadMedida', models.CharField(choices=[('kg', 'Kilogramos'), ('unid', 'Unidades')], max_length=4)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('pasteleria', 'Pasteleria'), ('panaderia', 'Panaderia')], max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
