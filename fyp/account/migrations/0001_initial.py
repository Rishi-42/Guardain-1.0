# Generated by Django 3.2.9 on 2022-06-06 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('user_type', models.CharField(blank=True, max_length=30, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Type_user',
            fields=[
                ('is_administrator', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_pharmacist', models.BooleanField(default=False)),
                ('is_counsellor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacistDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(upload_to='profile/pharmacist_profile_image')),
                ('pharmacy_email', models.EmailField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('registration_no', models.CharField(max_length=15, unique=True)),
                ('registered_doc', models.FileField(upload_to='doc/pharmacist_registred_document')),
                ('work_start', models.CharField(max_length=2)),
                ('work_end', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CounsellorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsellor_name', models.CharField(max_length=100, unique=True)),
                ('profile_image', models.ImageField(upload_to='profile/counsellor_profile_image')),
                ('counsellor_email', models.EmailField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('registration_no', models.CharField(max_length=15, unique=True)),
                ('registered_doc', models.FileField(upload_to='doc/counsellor_registred_document')),
                ('work_start', models.CharField(max_length=2)),
                ('work_end', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
