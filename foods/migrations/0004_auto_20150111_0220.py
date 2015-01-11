# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_daymeals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daymeals',
            options={'verbose_name_plural': 'Day meals'},
        ),
        migrations.AddField(
            model_name='foodserving',
            name='cholesterol',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='foodserving',
            name='sugar',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
