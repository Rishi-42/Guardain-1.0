# Generated by Django 3.2.9 on 2022-03-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_rename_pharmacy_name_add_product_pharmacy_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='cost',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
