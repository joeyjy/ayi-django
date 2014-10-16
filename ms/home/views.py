import os
import time
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from accounts.utils import DefaultDate

def index(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        print post_data
        if post_data['clean_date'] and post_data['clean_time']:
            book_time = post_data['clean_date'] + ' ' + post_data['clean_time']
            conv = time.strptime(book_time,"%d %b %Y %H:%M")
            request.session['booking_time'] = time.strftime('%Y-%m-%d %H:%M',conv)
            print request.session['booking_time']
            print book_time
            if request.user.id:
                return HttpResponseRedirect(reverse('clean_needs'))
            else:
                return HttpResponseRedirect(reverse('clean_info'))
    default_date = DefaultDate()
    return render_to_response('home/index.html',
                                  RequestContext(request, locals()))

def clean_info(request):
    pass

    return render_to_response('home/info.html',
                                  RequestContext(request, locals()))
                                  
def privacy_policy(request):
    pass

    return render_to_response('home/policy.html',
                                  RequestContext(request, locals()))

def merry_faq(request):
    pass

    return render_to_response('home/faq.html',
                                  RequestContext(request, locals()))
                                  
def about_us(request):
    pass

    return render_to_response('home/about.html',
                                  RequestContext(request, locals()))
