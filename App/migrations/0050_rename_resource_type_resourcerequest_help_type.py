# Generated by Django 5.0.3 on 2025-05-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0049_alert_emergency_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcerequest',
            old_name='resource_type',
            new_name='help_type',
        ),
    ]
