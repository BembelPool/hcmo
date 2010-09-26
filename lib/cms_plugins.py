# -*- coding:utf-8 -*-
#

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms.models.pluginmodel import CMSPlugin

from models import SponsorPlugin

class CMSSponsorPlugin(CMSPluginBase):
    model = SponsorPlugin
    name = 'Sponsoren'
    render_template = 'sponsor_entry.html'
    
    def render(self, context, instance, placeholder):
        context.update({'sponsor' : instance})
        return context
    
plugin_pool.register_plugin(CMSSponsorPlugin)



