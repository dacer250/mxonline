# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=500, verbose_name='访问地址'),
        ),
    ]