# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-14 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210514_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password_1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password_2',
        ),
    ]
