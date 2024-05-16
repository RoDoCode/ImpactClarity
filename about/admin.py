from django.contrib import admin
from .models import About, Resource


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'about_image',
        'updated_on',
        'content_1',
        'content_2',
        'content_3',
    )


admin.site.register(About, AboutAdmin)
admin.site.register(Resource)