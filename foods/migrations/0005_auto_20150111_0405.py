# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20150111_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date(2015, 1, 11))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DayHasFoodCombo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('food_combo', models.ForeignKey(to='foods.FoodCombo')),
                ('log', models.ForeignKey(to='foods.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DayHasFoodServing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('food_serving', models.ForeignKey(to='foods.FoodServing')),
                ('log', models.ForeignKey(to='foods.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DayHasMeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('log', models.ForeignKey(to='foods.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('food_combos', models.ManyToManyField(to='foods.FoodCombo')),
            ],
            options={
                'verbose_name_plural': 'Day meals',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='daymeals',
            name='food_combos',
        ),
        migrations.DeleteModel(
            name='DayMeals',
        ),
        migrations.AddField(
            model_name='dayhasmeal',
            name='meal',
            field=models.ForeignKey(to='foods.Meal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day',
            name='food_combos',
            field=models.ManyToManyField(to='foods.FoodCombo', through='foods.DayHasFoodCombo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day',
            name='food_servings',
            field=models.ManyToManyField(to='foods.FoodServing', through='foods.DayHasFoodServing', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day',
            name='meals',
            field=models.ManyToManyField(to='foods.Meal', through='foods.DayHasMeal', blank=True),
            preserve_default=True,
        ),
    ]
