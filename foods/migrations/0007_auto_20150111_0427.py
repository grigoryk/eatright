# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20150111_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayhasfoodcombo',
            old_name='food_combo',
            new_name='food_serving',
        ),
        migrations.RenameField(
            model_name='dayhasfoodcombo',
            old_name='amount',
            new_name='number_of_servings',
        ),
        migrations.RenameField(
            model_name='dayhasfoodserving',
            old_name='amount',
            new_name='number_of_servings',
        ),
        migrations.RenameField(
            model_name='dayhasmeal',
            old_name='meal',
            new_name='food_serving',
        ),
        migrations.RenameField(
            model_name='dayhasmeal',
            old_name='amount',
            new_name='number_of_servings',
        ),
    ]
