# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-04 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0016_myprojects_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprojects',
            name='short_description',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]