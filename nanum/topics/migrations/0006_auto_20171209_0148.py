# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20171208_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
