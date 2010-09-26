# -*- coding:utf-8 -*-
#

from django.contrib import admin

from models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('_image_repr', '_image_repr_hover', 'alt', 'link')
    

admin.site.register(Sponsor, SponsorAdmin)