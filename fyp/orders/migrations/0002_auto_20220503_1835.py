# Generated by Django 3.2.9 on 2022-05-03 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='country',
            new_name='building',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='province',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='zip_code',
            new_name='street',
        ),
    ]
