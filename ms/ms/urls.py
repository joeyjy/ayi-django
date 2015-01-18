from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from userena import views as userena_views
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^$', 'home.views.index', name='home_index'),
    url(r'^contact-info/$', userena_views.signup, name='clean_info'),
    url(r'^clean-needs/$', 'booking.views.clean_needs', name='clean_needs'),
    url(r'^pay/$', 'booking.views.pay', name='pay'),
    url(r'^make-confirm/$', 'booking.views.handle_confirm', name='handle_confirm'),
    #url(r'^history/(?P<username>[\.\w-]+)$', 'booking.views.history', name='booking_history'),
    # Examples:
    # url(r'^$', 'ms.views.home', name='home'),
    # url(r'^ms/', include('ms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^ayi/', include('accounts.urls')),
    url(r'^privacy-policy/', 'home.views.privacy_policy', name='privacy_policy'),
    url(r'^faq/', 'home.views.merry_faq', name='merry_faq'),
    url(r'^about-us/', 'home.views.about_us', name='about_us'),
    url(r'^lang/(?P<lang>\w+)/', 'home.views.switch_to_cn', name='switch_to_cn'),
    url(r'^payment/(?P<id>\d+)/$', "booking.views.payment", name="online_pay"),
    url(r'^alipay_notify_endpoint/$', "booking.views.alipay_notify", name="alipay_notify_endpoint"),
    url(r'^unipay_notify_endpoint/(?P<id>\d+)/$', "booking.views.unipay_notify", name="unipay_notify_endpoint"),
)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
