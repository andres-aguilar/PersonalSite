# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-09 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_auto_20181208_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]
