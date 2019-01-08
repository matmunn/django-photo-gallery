from django.contrib import admin
from django.utils.html import format_html

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'thumbnail',
    )

    def thumbnail(self, obj):
        return format_html(
            '<div style="background-image: url(\'/{}\'); width: 150px; '
            'height: 150px; background-size: cover; '
            'background-position: center center;"></div>'.format(
                obj.image.url)
        )
