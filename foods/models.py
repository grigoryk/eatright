from datetime import date

from django.db import models

import aggregators


class FoodServing(models.Model):
    name = models.CharField(max_length=255)
    serving_name = models.CharField(max_length=255, blank=True)

    calories = models.FloatField()
    fat = models.FloatField()
    cholesterol = models.FloatField(default=0)
    sodium = models.FloatField()
    carbs = models.FloatField()
    fibre = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        if self.serving_name:
            return "{0}, {1}".format(self.name, self.serving_name)

        else:
            return self.name

    def macro_ratio(self):
        return aggregators.macro_ratio(self.fat, self.carbs, self.protein)


class FoodCombo(models.Model, aggregators.WithAggregatedProperties):
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(FoodServing, through="FoodComboHasServing")

    def __str__(self):
        return self.name

    def get_aggregator(self):
        return aggregators.with_amount

    def get_list(self):
        return self.foodcombohasserving_set.all()


class Meal(models.Model, aggregators.WithAggregatedProperties):
    name = models.CharField(max_length=255)
    food_combos = models.ManyToManyField(FoodCombo)

    def __str__(self):
        return self.name

    def get_aggregator(self):
        return aggregators.basic

    def get_list(self):
        return self.food_combos.all()


class FoodComboHasServing(models.Model):
    food_combo = models.ForeignKey(FoodCombo)
    item = models.ForeignKey(FoodServing)
    amount = models.FloatField(default=1)


class Day(models.Model, aggregators.WithAggregatedProperties):
    date = models.DateField(default=date.today())
    meals = models.ManyToManyField(Meal, blank=True, through="DayHasMeal")
    food_servings = models.ManyToManyField(
        FoodServing, blank=True, through="DayHasFoodServing")
    food_combos = models.ManyToManyField(
        FoodCombo, blank=True, through="DayHasFoodCombo")

    def __str__(self):
        return "Log for {0}".format(self.date)

    def get_aggregator(self):
        return aggregators.daily_set

    def get_list(self):
        return [
            self.dayhasmeal_set.all(),
            self.dayhasfoodcombo_set.all(),
            self.dayhasfoodserving_set.all()
        ]


class DayHasMeal(models.Model):
    day = models.ForeignKey(Day)
    item = models.ForeignKey(Meal)
    amount = models.FloatField(default=1)


class DayHasFoodServing(models.Model):
    day = models.ForeignKey(Day)
    item = models.ForeignKey(FoodServing)
    amount = models.FloatField(default=1)


class DayHasFoodCombo(models.Model):
    day = models.ForeignKey(Day)
    item = models.ForeignKey(FoodCombo)
    amount = models.FloatField(default=1)
