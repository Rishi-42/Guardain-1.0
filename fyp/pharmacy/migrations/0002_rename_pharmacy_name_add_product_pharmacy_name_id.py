# Generated by Django 3.2.9 on 2022-03-04 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_product',
            old_name='pharmacy_name',
            new_name='pharmacy_name_id',
        ),
    ]