# Generated by Django 3.2.9 on 2022-04-12 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220412_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='meeting_created_by',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='meeting_location',
        ),
    ]
