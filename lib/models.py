# -*- coding: utf-8 -*-
# 
from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Sponsor(CMSPlugin):
    image = models.ImageField(upload_to="sponsoren/")
    image_hover = models.ImageField(upload_to="sponsoren/")
    alt = models.CharField(max_length="100")
    link =  models.URLField(blank=True)
    
    
