# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodserving',
            name='calories',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodserving',
            name='carbs',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodserving',
            name='fat',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodserving',
            name='fibre',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodserving',
            name='protein',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodserving',
            name='sodium',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
