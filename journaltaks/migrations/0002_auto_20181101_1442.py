# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-01 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journaltaks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=11, verbose_name='手机号'),
        ),
    ]
