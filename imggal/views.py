# -*- coding:utf-8 -*-
#

from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from models import Gallery


    
def get_images_for(request, gallery_id=False):
    print "get_images_for"
    if not gallery_id:
        raise Http404
    
    print "get gal"
    gallery = Gallery.objects.get(pk=gallery_id)
    print "render"
    return render_to_response("gallery.html", {'gallery':gallery })