from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview",]

    def get_preview(self,obj):
        height = obj.image.height
        width = obj.image.width
        if height > 200:
            img_ratio = height/width
            height = 200
            width = height/img_ratio

        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,)
        )

    fields = ('image','get_preview','position')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)