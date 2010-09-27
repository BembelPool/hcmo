# -*- coding:utf-8 -*-
#

from django.db import models




class EntryManager(models.Manager):
     def get_query_set(self):
        return super(EntryManager, self).get_query_set().filter(published=True)


class Entry(models.Model):
    title = models.CharField("Titel", max_length=100)
    slug = models.CharField("Slug", max_length=100)
    published = models.BooleanField("Veröffentlicht", default=False)
    posted = models.DateField("Datum")
    image = models.ImageField("Bild", upload_to="news_images/")
    
    teaser = models.TextField("Teaser")
    message = models.TextField("Nachricht")
    
    def __unicode__(self):
        return u"%s" % self.title
    
    def _image_repr(self):
        return '<img src="/site_media/%s" width="80" height="50" />' % self.image
    _image_repr.short_description = "Image"
    _image_repr.allow_tags = True
    
    class Meta:
        ordering = ('-published',)
    