# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps2', '0002_auto_20170621_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=45),
        ),
    ]
