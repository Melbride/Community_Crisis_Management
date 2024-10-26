# Generated by Django 5.0.6 on 2024-10-17 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_resourcerequest_location_resourcerequest_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcerequest',
            old_name='Resource_type',
            new_name='resource_type',
        ),
        migrations.AlterField(
            model_name='resourcerequest',
            name='phoneNumber',
            field=models.CharField(default='', max_length=17, validators=[django.core.validators.RegexValidator(message='Only numeric values are allowed', regex='^\\d*$')]),
        ),
    ]