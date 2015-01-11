from django.db import models


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


class FoodCombo(models.Model):
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(FoodServing, through="FoodComboHasServing")

    def __str__(self):
        return self.name

    def calories(self):
        return self.aggregate_food_properties('calories')

    def cholesterol(self):
        return self.aggregate_food_properties('cholesterol')

    def sugar(self):
        return self.aggregate_food_properties('sugar')

    def fat(self):
        return self.aggregate_food_properties('fat')

    def sodium(self):
        return self.aggregate_food_properties('sodium')

    def carbs(self):
        return self.aggregate_food_properties('carbs')

    def fibre(self):
        return self.aggregate_food_properties('fibre')

    def protein(self):
        return self.aggregate_food_properties('protein')

    def aggregate_food_properties(self, food_property):
        return reduce(
            lambda total, per_food: total + per_food,

            map(
                lambda combo_has_serving: getattr(combo_has_serving.food_serving, food_property) * combo_has_serving.number_of_servings,
                self.foodcombohasserving_set.all()
            )
        )


class DayMeals(models.Model):
    name = models.CharField(max_length=255)
    food_combos = models.ManyToManyField(FoodCombo)

    class Meta:
        verbose_name_plural = 'Day meals'

    def __str__(self):
        return self.name

    def calories(self):
        return self.aggregate_combo_properties('calories')

    def cholesterol(self):
        return self.aggregate_combo_properties('cholesterol')

    def sugar(self):
        return self.aggregate_combo_properties('sugar')

    def fat(self):
        return self.aggregate_combo_properties('fat')

    def sodium(self):
        return self.aggregate_combo_properties('sodium')

    def carbs(self):
        return self.aggregate_combo_properties('carbs')

    def fibre(self):
        return self.aggregate_combo_properties('fibre')

    def protein(self):
        return self.aggregate_combo_properties('protein')

    def aggregate_combo_properties(self, combo_property):
        return reduce(
            lambda total, per_combo: total + per_combo,

            map(
                lambda combo: getattr(combo, combo_property)(),
                self.food_combos.all()
            )
        )


class FoodComboHasServing(models.Model):
    food_serving = models.ForeignKey(FoodServing)
    food_combo = models.ForeignKey(FoodCombo)
    number_of_servings = models.FloatField(default=1)
