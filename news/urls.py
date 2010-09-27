# -*- coding:utf-8 -*-
#

from django.conf.urls.defaults import *
from news.views import *
    
urlpatterns = patterns('',
    (r'^/$', index),
    (r'^(?P<slug>[0-9A-Za-z-_.]+)', details),
)
