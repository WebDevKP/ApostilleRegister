# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_auto_20160408_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apostillerequest',
            name='is_open',
        ),
        migrations.AddField(
            model_name='apostillerequest',
            name='status',
            field=models.CharField(choices=[('p', 'pending'), ('a', 'approved'), ('r', 'rejected')], default='p', max_length=1),
        ),
    ]
