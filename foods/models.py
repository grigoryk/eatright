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


class FoodCombo(models.Model, aggregators.WithAggregatedProperties):
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(FoodServing, through="FoodComboHasServing")

    def __str__(self):
        return self.name

    def get_aggregator(self):
        return aggregators.servings

    def get_list(self):
        return self.foodcombohasserving_set.all()


class Meal(models.Model, aggregators.WithAggregatedProperties):
    name = models.CharField(max_length=255)
    food_combos = models.ManyToManyField(FoodCombo)

    def __str__(self):
        return self.name

    def get_aggregator(self):
        return aggregators.combos

    def get_list(self):
        return self.food_combos.all()


class FoodComboHasServing(models.Model):
    food_serving = models.ForeignKey(FoodServing)
    food_combo = models.ForeignKey(FoodCombo)
    number_of_servings = models.FloatField(default=1)


class Day(models.Model, aggregators.WithAggregatedProperties):
    date = models.DateField(default=date.today())
    meals = models.ManyToManyField(Meal, blank=True, through="DayHasMeal")
    food_servings = models.ManyToManyField(
        FoodServing, blank=True, through="DayHasFoodServing")
    food_combos = models.ManyToManyField(
        FoodCombo, blank=True, through="DayHasFoodCombo")

    def __str__(self):
        return "Log for {0}".format(self.when)

    def get_aggregator(self):
        return aggregators.daily_set

    def get_list(self):
        return [
            self.dayhasmeal_set.all(),
            self.dayhasfoodcombo_set.all(),
            self.dayhasfoodserving_set.all()
        ]


class DayHasMeal(models.Model):
    log = models.ForeignKey(Day)
    meal = models.ForeignKey(Meal)
    amount = models.FloatField()


class DayHasFoodServing(models.Model):
    log = models.ForeignKey(Day)
    food_serving = models.ForeignKey(FoodServing)
    amount = models.FloatField()


class DayHasFoodCombo(models.Model):
    log = models.ForeignKey(Day)
    food_combo = models.ForeignKey(FoodCombo)
    amount = models.FloatField()
