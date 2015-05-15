# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0010_auto_20150112_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodserving',
            name='price_per_serving',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date(2015, 1, 14)),
            preserve_default=True,
        ),
    ]
