# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='ganre',
            new_name='genre',
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='release date'),
        ),
    ]
