# Generated by Django 3.2.9 on 2022-05-03 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_order_id_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='Payment',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment'),
        ),
    ]