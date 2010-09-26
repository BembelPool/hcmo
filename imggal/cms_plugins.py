# -*- coding: utf-8 -*-
#

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from models import Gallery

class CMSShowroomGalleryPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'Showroom Gallery'
    render_template = 'gallery_plugin.html'
    
    def render(self, context, instance, placeholder):
        galleries = Gallery.objects.all()
        first_gallery = galleries[0]
        
        context.update({'first_gallery':first_gallery,
                        'galleries': galleries})
        return context
    
plugin_pool.register_plugin(CMSShowroomGalleryPlugin)