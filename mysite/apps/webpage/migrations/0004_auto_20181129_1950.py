# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_myprojects_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprojects',
            name='date',
            field=models.DateField(),
        ),
    ]
