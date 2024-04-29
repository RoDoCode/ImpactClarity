from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image_url',
        'video_url',
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
        'categories',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)