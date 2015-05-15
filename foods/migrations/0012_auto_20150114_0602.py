# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20150114_0600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodserving',
            old_name='price_per_serving',
            new_name='price',
        ),
    ]
