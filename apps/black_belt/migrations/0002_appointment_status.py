# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_belt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]