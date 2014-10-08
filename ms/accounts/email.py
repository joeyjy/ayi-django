from django.conf import settings
from django.template.loader import get_template, render_to_string
from django.template import Context
from .utils import send_mail_via_tencent

def create_mail_welcome(user):
    subject = 'Welcome to Merry Services'

    context = Context({
        'username': user.get_full_name(),
    })
    template = 'email/welcome.txt'
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
    
def create_mail_book_confirm(user, obj):
    subject = 'Merry Cleaning Services - Booking Confirmation'

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'hours': obj.hour,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
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

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'hours': obj.hour,
        'phone': user.my_profile.mobile,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
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

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'hours': obj.hour,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
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

    context = Context({
        'firstname': user.first_name,
        'lastname': user.last_name,
        'hours': obj.hour,
        'phone': user.my_profile.mobile,
        'street_num': user.my_profile.street_num,
        'street': user.my_profile.street,
        'bldg_num': user.my_profile.bldg_num,
        'apt_num': user.my_profile.apt_num,
        'cross': user.my_profile.cross,
        'area': user.my_profile.get_area_display(),
        'compound': user.my_profile.compound,
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