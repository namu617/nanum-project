# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171124_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('FB', 'Facebook'), ('EM', 'Email')], default='EM', max_length=2),
        ),
    ]
