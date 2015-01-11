from django.db import models


class FoodServing(models.Model):
    name = models.CharField(max_length=255)
    serving_name = models.CharField(max_length=255, blank=True)

    calories = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fibre = models.FloatField()
    protein = models.FloatField()
    sodium = models.FloatField()

    def __str__(self):
        return self.name


class FoodCombo(models.Model):
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(FoodServing, through="FoodComboHasServing")

    def __str__(self):
        return self.name


class FoodComboHasServing(models.Model):
    food_serving = models.ForeignKey(FoodServing)
    food_combo = models.ForeignKey(FoodCombo)
    number_of_servings = models.FloatField(default=1)
