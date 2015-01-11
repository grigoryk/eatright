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


def basic(food_property, item_list):
    return reduce(
        lambda total, per_combo: total + per_combo,

        map(
            lambda combo: getattr(combo, food_property)(),
            item_list
        )
    )


def with_amount(food_property, item_list):
    if len(item_list) == 0:
        return 0

    return reduce(
        lambda total, per_food: total + per_food,

        map(
            lambda has_serving: get_property(has_serving.item, food_property) * has_serving.amount,
            item_list
        )
    )


def daily_set(food_property, sets):
    meals, food_combos, food_servings = sets

    to_reduce = [
        with_amount(food_property, meals),
        with_amount(food_property, food_combos),
        with_amount(food_property, food_servings)
    ]

    return reduce(lambda total, per_set: total + per_set, to_reduce)


def get_property(item, property_name):
    prop = getattr(item, property_name)

    if type(prop) is float:
        return prop

    return prop()
