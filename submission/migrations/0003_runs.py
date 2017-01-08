# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20170107_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField(db_index=True)),
                ('language', models.CharField(choices=[(b'C', b'C'), (b'C++', b'C++'), (b'Java', b'Java'), (b'python', b'python')], max_length=5)),
                ('pid', models.IntegerField()),
                ('tid', models.IntegerField()),
                ('time', models.FloatField(blank=True)),
                ('result', models.CharField(blank=True, max_length=5)),
                ('submittime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]