# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_auto_20181129_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('carrer', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('profile', models.ForeignKey(to='webpage.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'tech/')),
            ],
        ),
    ]
