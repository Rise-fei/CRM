# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-08 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpermission', '0004_auto_20181108_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='file_file',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='essay',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpermission.File'),
        ),
    ]
