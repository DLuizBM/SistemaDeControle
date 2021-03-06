# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-14 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default=' ', max_length=20, verbose_name='Endere\xe7o'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='complement',
            field=models.CharField(default=' ', max_length=20, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='district',
            field=models.CharField(default=' ', max_length=20, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.CharField(default=' ', max_length=4, verbose_name='N\xfamero'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password_1',
            field=models.CharField(default='esoft123456', max_length=20, verbose_name='Senha'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password_2',
            field=models.CharField(default='esoft123456', max_length=20, verbose_name='Confirmar senha'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(default=' ', max_length=20, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='zipcode',
            field=models.CharField(default='12345678', max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(default=' ', max_length=20, verbose_name='Cidade'),
        ),
    ]
