# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20160318_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('job_start_date', models.DateField(verbose_name='Job start date')),
                ('job_finish_date', models.DateField(verbose_name='Job finish date')),
                ('position', models.CharField(max_length=75)),
                ('organ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Organ')),
                ('signet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.Signet')),
            ],
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
    ]
