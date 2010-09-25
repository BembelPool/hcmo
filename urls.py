from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),

    url(r'^aktuelles/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^', include('cms.urls')),
)
