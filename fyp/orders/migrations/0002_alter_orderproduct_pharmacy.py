# Generated by Django 3.2.9 on 2022-06-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='pharmacy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.pharmacistdetail'),
        ),
    ]
