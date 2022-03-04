# Generated by Django 3.2.9 on 2022-03-04 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.province')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('b_image', models.ImageField(blank=True, upload_to='images/')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.district')),
            ],
        ),
        migrations.CreateModel(
            name='Adresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_no', models.CharField(max_length=30)),
                ('tole', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.district')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.province')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
