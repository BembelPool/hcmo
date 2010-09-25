# -*- coding:utf-8 -*-
#

from django.db import models




class EntryManager(models.Manager):
     def get_query_set(self):
        return super(EntryManager, self).get_query_set().filter(published=True)


class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    posted = models.DateTimeField()
    image = models.ImageField(upload_to="news_images/")
    
    message = models.TextField()
    
    def _image_repr(self):
        return '<img src="/site_media/%s" width="80" height="50" />' % self.image
    _image_repr.short_description = "Image"
    _image_repr.allow_tags = True
    
    