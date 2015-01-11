# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCombo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodComboHasServing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_servings', models.FloatField(default=1)),
                ('food_combo', models.ForeignKey(to='foods.FoodCombo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodServing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('serving_name', models.CharField(max_length=255, blank=True)),
                ('calories', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('fibre', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('sodium', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='foodcombohasserving',
            name='food_serving',
            field=models.ForeignKey(to='foods.FoodServing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='foodcombo',
            name='foods',
            field=models.ManyToManyField(to='foods.FoodServing', through='foods.FoodComboHasServing'),
            preserve_default=True,
        ),
    ]
