import json
from django.http import HttpResponse
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import get_connection, send_mail


class TencentEmailBackend(EmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super(TencentEmailBackend, self).__init__(
            host=settings.TENCENT_EMAIL_HOST,
            port=settings.TENCENT_EMAIL_PORT,
            username=settings.TENCENT_EMAIL_USER,
            password=settings.TENCENT_EMAIL_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
            fail_silently=fail_silently, **kwargs
        )

def send_mail_via_tencent(subject, message, from_email, recipient_list, **kwargs):
    connection = get_connection(backend='accounts.utils.TencentEmailBackend')
    return send_mail(subject, message, from_email, recipient_list, connection=connection, **kwargs)

def JSONResponse(json_data, charset='utf-8', ensure_ascii=False, plain=False):
    mimetype = 'application/json'
    if plain:
        mimetype = 'text/plain'
    json_data = json.dumps((json_data), ensure_ascii=ensure_ascii)
    return HttpResponse(json_data, mimetype='%s; charset=%s' %(mimetype, charset))
