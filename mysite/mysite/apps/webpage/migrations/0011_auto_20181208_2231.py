# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-09 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0010_auto_20181201_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]