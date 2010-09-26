# -*- coding: utf-8 -*-
# 
from django.db import models
from cms.models.pluginmodel import CMSPlugin



class Sponsor(models.Model):
    image = models.ImageField(upload_to="sponsoren/")
    image_hover = models.ImageField(upload_to="sponsoren/")
    alt = models.CharField(max_length="100")
    link =  models.URLField(blank=True)
    
    def _image_repr(self):
        return '<img src="/site_media/%s" width="100" height="30" />' % self.image
    _image_repr.short_description = "Image"
    _image_repr.allow_tags = True

    def _image_repr_hover(self):
        return '<img src="/site_media/%s" width="100" height="30" />' % self.image_hover
    _image_repr_hover.short_description = "Image"
    _image_repr_hover.allow_tags = True
    
    
class SponsorPlugin(CMSPlugin):
    sponsoren = models.ManyToManyField(Sponsor)
    
    
class SubPageTeaserPlugin(CMSPlugin):
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='subpage')
    teaser = models.TextField()
    link = models.CharField(max_length=75, blank=True)
    
