from django.contrib import admin
from foods.models import FoodServing, FoodCombo, FoodComboHasServing, Meal, Day


class BaseWithProperties(admin.ModelAdmin):
    list_display = (
        'calories', 'fat', 'cholesterol', 'carbs', 'fibre', 'sugar',
        'protein', 'sodium')


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


class DayAdmin(BaseWithProperties):
    list_display = ('date',) + BaseWithProperties.list_display


# Register your models here.
admin.site.register(FoodServing, FoodServingAdmin)
admin.site.register(FoodCombo, FoodComboAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Day, DayAdmin)
