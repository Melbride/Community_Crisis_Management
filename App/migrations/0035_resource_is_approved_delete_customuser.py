# Generated by Django 5.1.3 on 2024-11-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]