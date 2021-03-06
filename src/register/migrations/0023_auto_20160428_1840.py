# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-28 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_auto_20160421_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apostille',
            name='document',
        ),
        migrations.RemoveField(
            model_name='apostille',
            name='icon',
        ),
        migrations.AddField(
            model_name='apostille',
            name='request',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.ApostilleRequest'),
        ),
        migrations.AddField(
            model_name='department',
            name='icon',
            field=models.ImageField(default='/media//apostille.jpg', upload_to=b''),
        ),
    ]
