from django.contrib import admin
from .models import (
    ImageInfo,
)
# Register your models here.

@admin.register(ImageInfo)
class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('image', 'cc_image', 'image_name', 'result')
