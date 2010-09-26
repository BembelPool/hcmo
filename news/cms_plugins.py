# -*- coding:utf-8 -*-
#

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from models import Entry



class CMSStartPageNewsPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'Startseiten News'
    render_template = 'start_page_news.html'
    
    def render(self, context, instance, placeholder):
        entries = Entry.objects.all()[:2]
        context.update({'sponsor' : instance,
                        'entries': entries})
        return context
    
plugin_pool.register_plugin(CMSStartPageNewsPlugin)
