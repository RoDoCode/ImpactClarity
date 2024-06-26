from django.contrib import admin
from .models import Product, Category, Series

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'video',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'series_no',
        'video',
        'screenshot_1',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
