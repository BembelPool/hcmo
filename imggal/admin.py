# -*- coding:utf-8 -*-
#

from django.contrib import admin

from models import Gallery, Photo

class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'published', 'created')
    

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('_image_repr','title', 'created')
   


admin.site.register(Photo, PhotoAdmin)

