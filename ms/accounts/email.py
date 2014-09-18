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
