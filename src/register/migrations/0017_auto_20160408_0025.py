# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 00:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20160408_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostillerequest',
            name='application_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 0, 25, 18, 811041), verbose_name='Application Date'),
        ),
    ]
