# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20150111_0427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayhasfoodcombo',
            old_name='number_of_servings',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='dayhasfoodcombo',
            old_name='log',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='dayhasfoodcombo',
            old_name='food_serving',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='dayhasfoodserving',
            old_name='number_of_servings',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='dayhasfoodserving',
            old_name='log',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='dayhasfoodserving',
            old_name='food_serving',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='dayhasmeal',
            old_name='number_of_servings',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='dayhasmeal',
            old_name='log',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='dayhasmeal',
            old_name='food_serving',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='foodcombohasserving',
            old_name='number_of_servings',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='foodcombohasserving',
            old_name='food_serving',
            new_name='item',
        ),
    ]
