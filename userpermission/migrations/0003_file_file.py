# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-08 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpermission', '0002_auto_20181107_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]