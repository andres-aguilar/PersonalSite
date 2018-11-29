# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprojects',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 29, 3, 54, 20, 141000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
