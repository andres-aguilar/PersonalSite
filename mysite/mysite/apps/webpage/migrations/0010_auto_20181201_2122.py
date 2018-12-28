# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_auto_20181130_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='description',
            field=models.CharField(default='nada', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='url',
            field=models.URLField(default='http://andres-aguilar.com'),
            preserve_default=False,
        ),
    ]
