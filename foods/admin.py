from django.contrib import admin
from foods.models import (
    FoodServing, FoodCombo, FoodComboHasServing, Meal,
    Day, DayHasMeal, DayHasFoodServing, DayHasFoodCombo)


class BaseWithProperties(admin.ModelAdmin):
    list_display = (
        'calories', 'fat', 'carbs', 'protein', 'cholesterol', 'fibre',
        'sugar', 'sodium')


class FoodServingAdmin(BaseWithProperties):
    list_display = ('name', 'serving_name') + BaseWithProperties.list_display
    save_as = True


class FoodComboHasServingInline(admin.TabularInline):
    model = FoodComboHasServing
    extra = 2


class FoodComboAdmin(BaseWithProperties):
    list_display = ('name',) + BaseWithProperties.list_display
    inlines = [FoodComboHasServingInline]
    save_as = True


class MealAdmin(BaseWithProperties):
    list_display = ('name',) + BaseWithProperties.list_display
    save_as = True


class DayHasMealInline(admin.TabularInline):
    model = DayHasMeal
    extra = 2


class DayHasFoodComboInline(admin.TabularInline):
    model = DayHasFoodCombo
    extra = 2


class DayHasFoodServingInline(admin.TabularInline):
    model = DayHasFoodServing
    extra = 2


class DayAdmin(BaseWithProperties):
    list_display = ('date',) + BaseWithProperties.list_display

    inlines = [
        DayHasMealInline,
        DayHasFoodComboInline,
        DayHasFoodServingInline
    ]


# Register your models here.
admin.site.register(FoodServing, FoodServingAdmin)
admin.site.register(FoodCombo, FoodComboAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Day, DayAdmin)
