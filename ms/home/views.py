from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    pass

    return render_to_response('home/index.html',
                                  RequestContext(request, locals()))

def clean_info(request):
    pass

    return render_to_response('home/info.html',
                                  RequestContext(request, locals()))

def clean_needs(request):
    pass

    return render_to_response('home/needs.html',
                                  RequestContext(request, locals()))
                                  