# coding: utf-8 

import os
import datetime
import time
import md5
from pytz import timezone

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.db.models import Q
from django.db.transaction import commit_on_success
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from alipay import Alipay

from accounts.email import create_sms, create_mail_book_confirm, create_mail_book_cancel, internal_book_confirm, internal_book_cancel
from accounts.models import Compound
from accounts.utils import JSONResponse, DefaultDate
from .models import Ayi
from booking.models import Booking

@staff_member_required
def ayi_index(request):
    ayis = Ayi.objects.filter()
    return render_to_response('accounts/ayi_index.html',
                                  RequestContext(request, locals()))

@staff_member_required
def revenue_results(request):
    ayis = Ayi.objects.filter()
    qs = Booking.objects.filter(status=2)
    data = request.GET.copy()
    if data.get('time'):
        time = data.get('time').split('-')
        qs = qs.filter(clean_time__year=time[0], clean_time__month=time[1])
    if data.get('ayi'):
        qs = qs.filter(clean_ayi__id=data.get('ayi'))
    revenue = qs.count()*35
    return render_to_response('accounts/revenue_index.html',
                                  RequestContext(request, locals()))