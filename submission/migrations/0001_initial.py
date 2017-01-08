# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=5, choices=[(b'C', b'C'), (b'C++', b'C++'), (b'Java', b'Java'), (b'python', b'python')])),
                ('code_upload', models.FileField(upload_to=b'')),
                ('code', models.TextField()),
            ],
        ),
    ]
