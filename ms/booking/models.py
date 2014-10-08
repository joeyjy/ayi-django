# coding: utf-8
import datetime
import os
import time


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext as _
from accounts.models import Ayi
from booking.constant import *
from booking.utils import CommonMixin

class Booking(CommonMixin, models.Model):
    booker = models.ForeignKey(User, db_index=True, verbose_name=u'Customer')
    status = models.IntegerField(choices=STATUS, null=True, blank=True)
    clean_ayi = models.ForeignKey(Ayi, null=True, blank=True, verbose_name=u'ayi')
    clean_time = models.DateTimeField(null=True, blank=True)
    bedroom = models.IntegerField(choices=BEDROOM_NUM, null=True, blank=True)
    bathroom = models.IntegerField(choices=BATHROOM_NUM, null=True, blank=True)
    laundry = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False, verbose_name=u'clean inside refrigerator')
    hand_wash = models.BooleanField(default=False, verbose_name=u'hand wash clothes')
    iron_clothe = models.BooleanField(default=False, verbose_name=u'iron clothes')
    hour = models.IntegerField(choices=HOUR, null=True, blank=True)
    message = models.TextField(validators=[MaxLengthValidator(300)], null=True, blank=True, verbose_name=u'SPECIAL INSTRUCTIONS')
    fee = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label='booking'
        verbose_name = 'All Booking'
        ordering = ['-id']

    def __unicode__(self):
        return self.booker.username
