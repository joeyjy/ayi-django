from django.conf.urls import *
from .views import *

urlpatterns = patterns('',
                       url(r'^$', ayi_index, name='ayi_index'),
                       url(r'^revenue/$', revenue_results, name='revenue_results'),
                       #url(r'^revenue/results/$', revenue_results, name='revenue_results'),
                       )