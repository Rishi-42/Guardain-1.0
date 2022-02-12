# Generated by Django 3.2.9 on 2022-02-11 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('OGRM_number', models.IntegerField()),
                ('INN_number', models.IntegerField()),
                ('licence_file', models.FileField(upload_to='photos/pharmacist_licence')),
                ('pharmacy_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('telephone_number', models.IntegerField()),
                ('pharmacy_email', models.EmailField(max_length=200)),
                ('estd_date', models.DateField()),
                ('registred_document', models.FileField(upload_to='photos/pharmacist_registred_document')),
                ('provience', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('zip', models.IntegerField()),
                ('profile_image', models.ImageField(upload_to='photos/pharmacist_profile_image')),
                ('working_days', models.CharField(max_length=200)),
                ('working_hours_start', models.TimeField()),
                ('working_hour_end', models.TimeField()),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='photos/product_images')),
                ('cost', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('dose_child', models.CharField(max_length=200)),
                ('dose_adult', models.CharField(max_length=200)),
                ('contraindiction', models.CharField(max_length=500)),
                ('indiction', models.CharField(max_length=500)),
                ('special_precautions', models.CharField(max_length=500)),
                ('adverse_effect', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.category')),
            ],
        ),
    ]
