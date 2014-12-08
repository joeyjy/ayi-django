# coding: utf-8 

import os
import datetime
import time

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.db.models import Q
from django.db.transaction import commit_on_success
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from alipay import Alipay

from accounts.email import create_mail_book_confirm, create_mail_book_cancel, internal_book_confirm, internal_book_cancel
from accounts.models import Compound
from accounts.utils import JSONResponse, DefaultDate
from .forms import BookingForm
from .models import Booking

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def pay(request):
    if request.session.get('pay_booking_id', False):
        item = Booking.objects.get(id=request.session['pay_booking_id'])
        fee = item.hour*35
    else:
        return HttpResponse('Pay without booking anything? :)')

    return render_to_response('booking/payment.html',
                                  RequestContext(request, locals()))

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def clean_needs(request):
    if not request.session.get('booking_time'):
        return HttpResponseRedirect(reverse('home_index'))
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = BookingForm(post_data)
        form.booker = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.booker = request.user
            obj.status = 4
            obj.clean_time = request.session.get('booking_time', '')
            obj.save()
            request.session['pay_booking_id'] = obj.id
            return HttpResponseRedirect(reverse('pay'))
        else:
            print form.errors
            print request.user
    else:
        form =BookingForm()
    if request.session.get('lang') == 'cn':
        return render_to_response('cn/booking/needs.html',
                                  RequestContext(request, locals()))
    return render_to_response('booking/needs.html',
                                  RequestContext(request, locals()))

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def history(request, username):
    if request.user.username != username and not request.user.has_perm('booking.change_booking'):
        raise PermissionDenied
    booking_list = Booking.objects.filter(Q(booker__username=username), Q(status=1) | Q(status=4) | Q(status=5))
    booking_pass = Booking.objects.filter(booker__username=username).exclude(Q(status=1) | Q(status=4) | Q(status=5))
    if booking_list:
        customer = booking_list[0].booker.username
    elif booking_pass:
        customer = booking_pass[0].booker.username
    else:
        customer = request.user.username
    default_date = DefaultDate()
    return render_to_response('booking/history.html',
                                  RequestContext(request, locals()))
                                  
@login_required(login_url='/accounts/signin/')
@csrf_exempt
def billing(request, username):
    if request.user.username != username and not request.user.has_perm('booking.change_booking'):
        raise PermissionDenied
    booking_list = Booking.objects.filter(booker__username=username)
    if booking_list:
        customer = booking_list[0].booker.username
    else:
        customer = request.user.username
    default_date = DefaultDate()
    return render_to_response('booking/billing.html',
                                  RequestContext(request, locals()))

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def booking_cancel(request, username, pk):
    if request.user.username != username and not request.user.has_perm('booking.change_booking'):
        raise PermissionDenied

    item = Booking.objects.get(id=pk)
    item.status = 3
    create_mail_book_cancel(item.booker, item)
    internal_book_cancel(item.booker, item)
    item.save()

    return HttpResponseRedirect(reverse('booking_history',args=[username]))

def compound_info(request, pk):
    compound = Compound.objects.get(id=pk)
    result = {'address':compound.street_address,
              'name':compound.street_name,
              'cross':compound.cross_street,
              'area':compound.district,}
    return JSONResponse(result)

@login_required(login_url='/accounts/signin/')
@csrf_exempt
def handle_confirm(request):
    if request.method == 'POST' and request.is_ajax():
        post_data = request.POST.copy()
        print post_data
        if request.session.get('pay_booking_id', False):
            item = Booking.objects.get(id=request.session['pay_booking_id'])
            item.status = 1
            item.save()
            create_mail_book_confirm(item.booker, item)
            internal_book_confirm(item.booker, item)
            return HttpResponse("Y")
    raise PermissionDenied
    
@commit_on_success
def payment(request, id):
    item = get_object_or_404(Booking, id=id)
    fee = item.hour*35
    url = lambda path: "".join(["http://", get_current_site(request).domain, path])
    if request.method == "POST":
        data = request.POST.copy()
        if data.get('pay_method', False) == '4':
            alipay = Alipay(pid=settings.ALIPAY_PID, key=settings.ALIPAY_KEY, seller_email=settings.ALIPAY_SELLER_EMAIL)
            url = alipay.create_direct_pay_by_user_url(
                        out_trade_no=item.id,
                        subject='Merry clean service',
                        total_fee=1,
                        return_url=url(reverse('userena_profile_edit',args=[item.booker.username])),
                        notify_url=url("/alipay_notify_endpoint/"))

            return render_to_response("booking/alipay.html", {"url": url})
    return HttpResponseBadRequest()

@csrf_exempt
def alipay_notify(request):
    """ Notify callback for alipay """
    alipay = Alipay(pid=settings.ALIPAY_PID, key=settings.ALIPAY_KEY, seller_email=settings.ALIPAY_SELLER_EMAIL)
    if alipay.verify_notify(**dict(request.POST.items())):
        if request.POST.get("trade_status") in ["WAIT_SELLER_SEND_GOODS", "TRADE_SUCCESS"]:
            order = Booking.objects.get(id=request.POST.get("out_trade_no"))
            order.status = 5
            order.save()
            create_mail_book_confirm(order.booker, order)
            internal_book_confirm(order.booker, order)
            return HttpResponse('success')
        else:
            print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    return HttpResponse('failure')