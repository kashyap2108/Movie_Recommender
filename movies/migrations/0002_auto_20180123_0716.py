# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(default=2000),
        ),
    ]