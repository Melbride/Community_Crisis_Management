# Generated by Django 5.0.3 on 2025-07-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0055_profile_account_type_profile_donor_since_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='donor_tier',
            field=models.CharField(blank=True, choices=[('basic', 'Basic Supporter'), ('standard', 'Standard Donor'), ('premium', 'Premium Supporter')], max_length=50, null=True),
        ),
    ]
