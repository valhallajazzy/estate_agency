# Generated by Django 2.2.24 on 2024-01-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20240117_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
