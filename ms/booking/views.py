# coding: utf-8 

import os
import datetime
import time

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from accounts.email import create_mail_book_confirm, create_mail_book_cancel, internal_book_confirm, internal_book_cancel
from accounts.models import Compound
from accounts.utils import JSONResponse
from .forms import BookingForm
from .models import Booking

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def clean_needs(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = BookingForm(post_data)
        form.booker = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.booker = request.user
            obj.status = 1
            obj.save()
            create_mail_book_confirm(obj.booker, obj)
            internal_book_confirm(obj.booker, obj)
            return HttpResponse('ok, need to process Alipay')
        else:
            print form.errors
            print request.user
    else:
        form =BookingForm()

    return render_to_response('booking/needs.html',
                                  RequestContext(request, locals()))

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def history(request, username):
    if request.user.username != username and not request.user.has_perm('auth.change_booking'):
        raise PermissionDenied
    booking_list = Booking.objects.filter(booker__username=username)
    #os.environ['TZ'] = 'Asia/Shanghai'
    #time.tzset()
    default_time = int(time.strftime('%H'))+4
    if default_time > 20:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        default_date = tomorrow.strftime('%d %b %Y')
    else:
        default_date = datetime.date.today().strftime('%d %b %Y')

    return render_to_response('booking/history.html',
                                  RequestContext(request, locals()))
                                  
@login_required(login_url='/accounts/signin/')
@csrf_exempt
def billing(request, username):
    if request.user.username != username and not request.user.has_perm('auth.change_booking'):
        raise PermissionDenied
    booking_list = Booking.objects.filter(booker__username=username)
    
    #os.environ['TZ'] = 'Asia/Shanghai'
    #time.tzset()
    default_time = int(time.strftime('%H'))+4
    if default_time > 20:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        default_date = tomorrow.strftime('%d %b %Y')
    else:
        default_date = datetime.date.today().strftime('%d %b %Y')

    return render_to_response('booking/billing.html',
                                  RequestContext(request, locals()))

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def booking_cancel(request, username, pk):
    if request.user.username != username and not request.user.has_perm('auth.change_booking'):
        raise PermissionDenied

    try:
        item = Booking.objects.get(id=pk)
        item.status = 3
        create_mail_book_cancel(request.user, item)
        internal_book_cancel(request.user, item)
        item.save()
    except:
        HttpResponse('Error! Please contact administrator')
    return HttpResponseRedirect(reverse('booking_history',args=[username]))

def compound_info(request, pk):
    compound = Compound.objects.get(id=pk)
    result = {'address':compound.street_address,
              'name':compound.street_name,
              'cross':compound.cross_street,
              'area':compound.district,}
    return JSONResponse(result)
