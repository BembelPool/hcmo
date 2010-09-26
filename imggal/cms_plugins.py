# -*- coding: utf-8 -*-
#

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from models import Gallery, GalleryPlugin, Photo, NewPhotosPlugin

class CMSShowroomGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = 'Showroom Gallery'
    render_template = 'gallery_plugin.html'
    
    def render(self, context, instance, placeholder):
        galleries = instance.galleries.all()
        context.update({'galleries': galleries})
        return context
    
plugin_pool.register_plugin(CMSShowroomGalleryPlugin)


class CMSNewPhotosPlugin(CMSPluginBase):
    model = NewPhotosPlugin
    name = '4 Neue Fotos'
    render_template = '4_new_fotos_plugin.html'
    
    def render(self, context, instance, placeholder):
        photos = Photo.objects.all()[:4]
        context.update({'photos':photos})
        return context
    
plugin_pool.register_plugin(CMSNewPhotosPlugin)