# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_auto_20160407_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apostillerequest',
            name='receiving_date',
        ),
        migrations.AddField(
            model_name='apostillerequest',
            name='application_date',
            field=models.DateTimeField(default='2015-12-27', verbose_name='Application Date'),
            preserve_default=False,
        ),
    ]
