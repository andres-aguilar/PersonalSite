# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_schools_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
