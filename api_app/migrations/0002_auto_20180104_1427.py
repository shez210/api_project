# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 09:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'managed': True,
                'verbose_name_plural': 'users',
            },
        ),
        migrations.AlterField(
            model_name='information',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 9, 27, 39, 444000, tzinfo=utc)),
        ),
    ]
