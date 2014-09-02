import json
from django.conf import settings                                                                                                            
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.core.paginator import Paginator
from django.contrib.contenttypes.models  import ContentType
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import ListView

from models import Booking
from booking.constant import *

class BookingForm(forms.ModelForm):                                                                                                             
    class Meta:
        model = Booking
        #widgets = {'appliances': forms.CheckboxSelectMultiple,
        #           'description': forms.Textarea(attrs={'placeholder': 'Description should be less than 300 words'})
        #}
        fields = ('bedroom', 'bathroom', 'laundry', 'hour', 'message',)
#    def __init__(self, *args, **kwargs):
#        super(RentForm, self).__init__(*args, **kwargs)
#        self.fields['metro'].widget = \
#            MetroWidget(template='housing/metro_select.html',
#                        metro=(self.instance.metro if self.instance.metro else ''),
#                    )
