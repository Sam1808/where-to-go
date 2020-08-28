from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html
from .models import Place, Image

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview",]

    def get_preview(self,obj):
        if not obj.image:
            return format_html('<b>No image<br>available</b>')
        
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


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
admin.site.register(Image, ImageAdmin)
