# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_auto_20150111_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date(2015, 1, 12)),
            preserve_default=True,
        ),
    ]
