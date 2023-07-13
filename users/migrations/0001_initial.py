# Generated by Django 4.2.3 on 2023-07-12 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.TextField(default=None, max_length=255)),
                ('last_name', models.TextField(default=None, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('my_country', models.TextField(default=None, max_length=255)),
                ('fav_countries', models.JSONField(default=None)),
                ('creation_date', models.DateTimeField(default=datetime.date(2023, 7, 12))),
                ('update_date', models.DateField(default=datetime.date(2023, 7, 12))),
                ('last_request', models.DateField(default=datetime.date(2023, 7, 12))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]