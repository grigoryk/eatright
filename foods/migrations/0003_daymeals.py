# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20150111_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayMeals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('food_combos', models.ManyToManyField(to='foods.FoodCombo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
