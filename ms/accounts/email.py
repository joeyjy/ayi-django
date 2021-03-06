# coding: utf-8

import time
from pytz import timezone

from django.conf import settings
from django.template.loader import get_template, render_to_string
from django.template import Context
from .utils import send_mail_via_tencent

def create_sms(user,obj,cancel=None):
    import requests
    url = 'http://api.sms.cn/mt/'
    date_obj = obj.clean_time.astimezone(timezone('Asia/Shanghai'))
    mobile = user.my_profile.mobile
    content = '您的预订已成功。若更改服务时间，请致电021-63801553。Booking Confirmed- at %s for %s hrs. Call 021-63801553 from 9AM to 6PM to make changes.【MCS清洁超人】' % (date_obj.strftime('%I:%M %p, %b %d, %Y'), obj.hour)
    if cancel:
        content = '您的预订已取消。期待您的下次预订。Booking Cancellation- at %s for %s hrs. Look forward to your next booking.【MCS清洁超人】' % (date_obj.strftime('%I:%M %p, %b %d, %Y'), obj.hour)
    payload = {'uid':settings.SMS_USER, 'pwd':settings.SMS_PWD, 'mobile':mobile, 'encode':'utf8', 'content':content}
    requests.post(url,data=payload)

def create_mail_welcome(user):
    subject = 'Merry Cleaning Services - Welcome!'

    context = Context({
        'username': user.first_name,
        'email': user.email,
    })
    template = 'email/welcome.txt'
    message = get_template(template).render(context)

    try:
        result = send_mail_via_tencent(subject, message , settings.TENCENT_FROM_EMAIL,
            [user.email], fail_silently=True)
    except Exception as e:
        print e
        #result = send_mail(subject, message , settings.DEFAULT_FROM_EMAIL,
        #    [user.email], fail_silently=True)
    return result
    
def create_mail_book_confirm(user, obj):
    subject = 'Merry Cleaning Services - Booking Confirmation'
    #date_obj = time.strptime(obj.clean_time,"%Y-%m-%d %H:%M")
    date_obj = obj.clean_time.astimezone(timezone('Asia/Shanghai'))
    
    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'day': date_obj.strftime('%A'),
        'date': date_obj.strftime('%b %d, %Y'),
        'time': date_obj.strftime('%I:%M %p'),
        'hours': obj.hour,
        'refrigerator': obj.refrigerator,
        'hand_wash': obj.hand_wash,
        'iron_clothe': obj.iron_clothe,
        'message': obj.message,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
        'status': obj.status,
        'type': obj.get_book_type_display(),
    })
    template = 'email/book_confirm.txt'
    message = get_template(template).render(context)

    try:
        result = send_mail_via_tencent(subject, message , settings.TENCENT_FROM_EMAIL,
            [user.email], fail_silently=True)
    except Exception as e:
        print e
        print "---------------------------------------"
        #result = send_mail(subject, message , settings.DEFAULT_FROM_EMAIL,
        #    [user.email], fail_silently=True)
    return result
    
def internal_book_confirm(user, obj):
    subject = 'NEW BOOKING - ('+user.my_profile.get_area_display()+'), '+user.get_full_name()
    #date_obj = time.strptime(obj.clean_time,"%Y-%m-%d %H:%M")
    date_obj = obj.clean_time.astimezone(timezone('Asia/Shanghai'))

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'day': date_obj.strftime('%A'),
        'date': date_obj.strftime('%b %d, %Y'),
        'time': date_obj.strftime('%I:%M %p'),
        'hours': obj.hour,
        'refrigerator': obj.refrigerator,
        'hand_wash': obj.hand_wash,
        'iron_clothe': obj.iron_clothe,
        'message': obj.message,
        'phone': user.my_profile.mobile,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
        'status': obj.status,
        'type': obj.get_book_type_display(),
    })
    template = 'email/internal_confirm.txt'
    message = get_template(template).render(context)

    try:
        result = send_mail_via_tencent(subject, message , settings.TENCENT_FROM_EMAIL,
            [settings.INTERNAL_BOOKINGS_EMAIL], fail_silently=True)
    except Exception as e:
        print e
        print "---------------------------------------"
        #result = send_mail(subject, message , settings.DEFAULT_FROM_EMAIL,
        #    [user.email], fail_silently=True)
    return result
    
def create_mail_book_cancel(user, obj):
    subject = 'Merry Cleaning Services - Booking Canceled'
    date_obj = obj.clean_time.astimezone(timezone('Asia/Shanghai'))

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'day': date_obj.strftime('%A'),
        'date': date_obj.strftime('%b %d, %Y'),
        'time': date_obj.strftime('%I:%M %p'),
        'hours': obj.hour,
        'refrigerator': obj.refrigerator,
        'hand_wash': obj.hand_wash,
        'iron_clothe': obj.iron_clothe,
        'message': obj.message,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
        'type': obj.get_book_type_display(),
    })
    template = 'email/book_cancel.txt'
    message = get_template(template).render(context)

    try:
        result = send_mail_via_tencent(subject, message , settings.TENCENT_FROM_EMAIL,
            [user.email], fail_silently=True)
    except Exception as e:
        print e
        print "---------------------------------------"
        #result = send_mail(subject, message , settings.DEFAULT_FROM_EMAIL,
        #    [user.email], fail_silently=True)
    return result

def internal_book_cancel(user, obj):
    subject = 'CANCELED BOOKING - ('+user.my_profile.get_area_display()+'), '+user.get_full_name()
    date_obj = obj.clean_time.astimezone(timezone('Asia/Shanghai'))

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'day': date_obj.strftime('%A'),
        'date': date_obj.strftime('%b %d, %Y'),
        'time': date_obj.strftime('%I:%M %p'),
        'hours': obj.hour,
        'refrigerator': obj.refrigerator,
        'hand_wash': obj.hand_wash,
        'iron_clothe': obj.iron_clothe,
        'message': obj.message,
        'phone': user.my_profile.mobile,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
        'type': obj.get_book_type_display(),
    })
    template = 'email/internal_cancel.txt'
    message = get_template(template).render(context)

    try:
        result = send_mail_via_tencent(subject, message , settings.TENCENT_FROM_EMAIL,
            [settings.INTERNAL_BOOKINGS_EMAIL], fail_silently=True)
    except Exception as e:
        print e
        print "---------------------------------------"
        #result = send_mail(subject, message , settings.DEFAULT_FROM_EMAIL,
        #    [user.email], fail_silently=True)
    return result
