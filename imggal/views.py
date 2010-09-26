# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response


def main(request):
    print "Main!"
    return render_to_response("showroom_gallery.html", { },
                              RequestContext(request))
    
    
def get_images_for(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    
    return render_to_response("", {'gallery':gallery },
                              RequestContext(request))