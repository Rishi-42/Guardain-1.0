# Generated by Django 3.2.9 on 2022-06-20 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderproduct_pharmacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='building',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
