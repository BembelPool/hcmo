# -*- coding:utf-8 -*-
#

from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext

from models import Entry

def single(request, id=False):
    if not id:
        raise Http404
    
    entry = Entry.objects.get(pk=id)
    return render_to_response("single.html", {'entry' : entry}, RequestContext(request))