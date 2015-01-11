# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20150111_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayhasfoodcombo',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dayhasfoodserving',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dayhasmeal',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
    ]
