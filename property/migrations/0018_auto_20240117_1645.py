# Generated by Django 2.2.24 on 2024-01-17 13:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20240117_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=12, null=True, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(blank=True, related_name='Owned_apartments', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
        migrations.DeleteModel(
            name='Own',
        ),
    ]