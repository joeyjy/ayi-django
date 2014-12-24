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
    clean_time = models.DateTimeField(null=True, blank=True, verbose_name=u'Clean Time')
    bedroom = models.IntegerField(choices=BEDROOM_NUM, null=True, blank=True)
    bathroom = models.IntegerField(choices=BATHROOM_NUM, null=True, blank=True)
    refrigerator = models.BooleanField(default=False, verbose_name=u'clean inside refrigerator')
    hand_wash = models.BooleanField(default=False, verbose_name=u'hand wash clothes')
    iron_clothe = models.BooleanField(default=False, verbose_name=u'iron clothes')
    hour = models.FloatField(choices=HOUR, null=True, blank=True, verbose_name=u'Hours')
    message = models.TextField(validators=[MaxLengthValidator(300)], null=True, blank=True, verbose_name=u'SPECIAL INSTRUCTIONS')
    fee = models.IntegerField(null=True, blank=True)
    pay_method = models.IntegerField(choices=PAYMETHOD, null=True, blank=True, verbose_name=u'payment')
    date_created = models.DateTimeField(null=True, blank=True, verbose_name='Date Created')
    date_modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label='booking'
        verbose_name = 'All Booking'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.booker.username

    def model_callable(self):
        return self.booker.compound.name
