# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_auto_20171206_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content_html',
            field=models.TextField(blank=True),
        ),
    ]