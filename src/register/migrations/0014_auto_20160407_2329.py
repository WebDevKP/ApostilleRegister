# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20160407_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='signer_patronymic',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='signer_surname',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='signer_name',
            field=models.CharField(max_length=50),
        ),
    ]
