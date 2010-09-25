# -*- coding:utf-8 -*-
#

from django.contrib import admin

from models import Entry

class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted'
    list_display = ('_image_repr', 'title', 'slug', 'published', 'posted')
    prepopulated_fields = {'slug' : ('title',) }

admin.site.register(Entry, EntryAdmin)