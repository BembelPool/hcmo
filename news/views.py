# -*- coding:utf-8 -*-
#

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

from models import Entry

def single(request, id=False):
    if not id:
        raise Http404
    
    entry = Entry.objects.get(pk=id)
    return render_to_response("single.html", {'entry' : entry}, RequestContext(request))
    
    
def index(request):
    entry = Entry.objects.all()[0]
    return HttpResponseRedirect("/news/" + entry.slug )
    
    
def details(request, slug):
    print "defauls"
    print slug
    details_entry= Entry.objects.filter(slug=slug)[0]
    print details_entry
    latest_entries = Entry.objects.all()[:5]
    print latest_entries
    return render_to_response("details.html", { 'details_entry': details_entry,
                                'latest ': latest_entries }, RequestContext(request))