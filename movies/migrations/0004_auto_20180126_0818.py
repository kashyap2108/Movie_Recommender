# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20180123_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]
