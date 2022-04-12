# Generated by Django 3.2.9 on 2022-04-11 20:48

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
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('client_age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=100)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=255)),
                ('meeting_description', models.TextField()),
                ('meeting_created_by', models.CharField(max_length=255)),
                ('client_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]