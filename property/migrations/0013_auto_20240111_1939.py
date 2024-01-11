# Generated by Django 2.2.24 on 2024-01-11 16:39

from django.db import migrations
import phonenumbers


def convert_and_set_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = flat.owners_phonenumber
        parse_phone_number = phonenumbers.parse(phone_number, "RU")
        if phonenumbers.is_valid_number(parse_phone_number):
            converted_phone_number = phonenumbers.format_number(parse_phone_number, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_pure_phone = converted_phone_number
            flat.save()
        else:
            flat.owner_pure_phone = None
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20240111_1938'),
    ]

    operations = [
        migrations.RunPython(convert_and_set_phonenumber)
    ]
