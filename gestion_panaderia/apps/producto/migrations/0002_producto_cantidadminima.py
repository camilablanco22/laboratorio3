# Generated by Django 5.1.2 on 2024-10-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidadMinima',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]