# -*- coding:utf-8 -*-
#

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    # Hacky ajax shit ... 
    (r'^news/single/(\d+)', 'news.views.single'),
    (r'^imggal/get_images_for/(\d+)', 'imggal.views.get_images_for'),


    (r'^', include('cms.urls')),
)
