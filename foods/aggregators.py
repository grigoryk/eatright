class WithAggregatedProperties:
    def calories(self):
        return self.get_aggregator()('calories', self.get_list())

    def cholesterol(self):
        return self.get_aggregator()('cholesterol', self.get_list())

    def sugar(self):
        return self.get_aggregator()('sugar', self.get_list())

    def fat(self):
        return self.get_aggregator()('fat', self.get_list())

    def sodium(self):
        return self.get_aggregator()('sodium', self.get_list())

    def carbs(self):
        return self.get_aggregator()('carbs', self.get_list())

    def fibre(self):
        return self.get_aggregator()('fibre', self.get_list())

    def protein(self):
        return self.get_aggregator()('protein', self.get_list())


def servings(food_property, serving_list):
    return reduce(
        lambda total, per_food: total + per_food,

        map(
            lambda combo_has_serving: getattr(combo_has_serving.food_serving, food_property) * combo_has_serving.number_of_servings,
            serving_list
        )
    )


def combos(combo_property, combo_list):
    return reduce(
        lambda total, per_combo: total + per_combo,

        map(
            lambda combo: getattr(combo, combo_property)(),
            combo_list
        )
    )


def daily_set(combo_property, sets):
    pass
