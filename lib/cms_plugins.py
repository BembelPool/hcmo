
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms.models.pluginmodel import CMSPlugin
from zinnia.models import Entry, Category
from models import Sponsor

class CMSSponsorPlugin(CMSPluginBase):
    model = Sponsor
    name = 'Sponsor'
    render_template = 'sponsor_entry.html'
    
    def render(self, context, instance, placeholder):
        context.update({'sponsor' : instance})
        return context
    
plugin_pool.register_plugin(CMSSponsorPlugin)


class CMSFancyLoadEntriesPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'Fancy Load Entries'
    render_template = 'fancy_news_entry.html'
    
    def render(self, context, instance, placeholder):
        entries = Entry.published.all()
        context.update({'sponsor' : instance,
                        'entries': entries})
        return context
    
plugin_pool.register_plugin(CMSFancyLoadEntriesPlugin)
