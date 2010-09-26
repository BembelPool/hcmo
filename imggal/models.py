# -*- coding:utf-8 -*-
#

from django.db import models



class GalleryManager(models.Manager):
    def get_query_set(self):
        return super(GalleryManager, self).get_query_set().filter(published=True)


class Gallery(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    
    admin_objects = models.Manager()
    objects = GalleryManager()

    def thumb(self):
        """ Get the first Photo from this gallery to display as thumb
        """
        try:
            photo = Photo.objects.filter(gallery=self.id)[0]
        except IndexError:
            pass
        else:
            return photo.image

    """
    def get_absolute_url(self):
        return ('myproject.gallery.views.photo_list', None, {'slug': self.slug})
    get_absolute_url = permalink(get_absolute_url)
    """

    def __unicode__(self):
        return self.title


class PhotoManager(models.Manager):
    def get_query_set(self):
        return super(PhotoManager, self).get_query_set().filter(gallery__published=True)


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery)
    image = models.ImageField(upload_to='imggal/')
    title = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    admin_objects = models.Manager()
    objects = PhotoManager()

    def __unicode__(self):
        return self.title
    
    def _image_repr(self):
        return '<img src="/site_media/%s" width="130" height="100" />' % self.image
    _image_repr.short_description = "Image"
    _image_repr.allow_tags = True

