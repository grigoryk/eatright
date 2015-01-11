from django.contrib import admin
from foods.models import FoodServing, FoodCombo, FoodComboHasServing


class FoodServingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'serving_name', 'calories', 'fat', 'carbs',
        'fibre', 'protein', 'sodium')


class FoodComboHasServingInline(admin.TabularInline):
    model = FoodComboHasServing
    extra = 2


class FoodComboAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'calories', 'fat', 'carbs',
        'fibre', 'protein', 'sodium')

    inlines = [FoodComboHasServingInline]


# Register your models here.
admin.site.register(FoodServing, FoodServingAdmin)
admin.site.register(FoodCombo, FoodComboAdmin)
