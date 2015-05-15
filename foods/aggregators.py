class WithAggregatedProperties:
    def macro_ratio(self):
        return macro_ratio(self.fat(), self.carbs(), self.protein())

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

    def price(self):
        return self.get_aggregator()('price', self.get_list())


def macro_ratio(fat, carbs, protein):
    total = fat + carbs + protein
    carb_perc = round((carbs / total), 3) * 100
    fat_perc = round((fat / total), 3) * 100
    protein_perc = round((protein / total), 3) * 100

    return "{0}% / {1}% / {2}%".format(int(fat_perc), int(carb_perc), int(protein_perc))


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

    return reduce(
        lambda total, per_set: total + per_set,

        map(
            lambda s: with_amount(food_property, s),
            sets
        )
    )


def get_property(item, property_name):
    prop = getattr(item, property_name)

    if type(prop) is float:
        return prop

    elif not prop:
        return 0

    return prop()
