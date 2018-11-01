# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-31 10:44
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userpermission.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=30)),
                ('job_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=30)),
                ('permission', models.ManyToManyField(to='userpermission.Permission')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userpermission.Job'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userpermission.Employee'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.ManyToManyField(to='userpermission.Role'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
