# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_auto_20171209_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_count',
            field=models.IntegerField(default=0),
        ),
    ]
