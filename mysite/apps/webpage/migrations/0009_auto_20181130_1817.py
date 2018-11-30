# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20181130_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologies',
            name='image',
            field=models.ImageField(upload_to=b'static/techs'),
        ),
    ]
