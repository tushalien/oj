# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20170128_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='id',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
