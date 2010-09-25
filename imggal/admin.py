# -*- coding:utf-8 -*-
#

from django.contrib import admin

from models import Gallery, Photo

class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'slug', 'published', 'created')
    prepopulated_fields = {'slug' : ('title',) }

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('_image_repr','title', 'slug', 'created')
    prepopulated_fields = {'slug' : ('title',) }


admin.site.register(Photo, PhotoAdmin)

