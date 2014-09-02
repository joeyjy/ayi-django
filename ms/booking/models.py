# coding: utf-8
import datetime
import os
import time


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext as _
from booking.constant import *
from booking.utils import CommonMixin

class Booking(CommonMixin, models.Model):
    booker = models.ForeignKey(User, db_index=True, verbose_name=u'booker')
    status = models.IntegerField(choices=STATUS, null=True, blank=True)
    clean_time = models.DateTimeField(null=True, blank=True)
    bedroom = models.IntegerField(choices=BEDROOM_NUM, null=True, blank=True)
    bathroom = models.IntegerField(choices=BATHROOM_NUM, null=True, blank=True)
    laundry = models.IntegerField(choices=LAUNDRY, null=True, blank=True)
    hour = models.IntegerField(choices=HOUR, null=True, blank=True)
    message = models.TextField(validators=[MaxLengthValidator(300)], null=True, blank=True)
    fee = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label='booking'

    def __unicode__(self):
        return self.booker.username