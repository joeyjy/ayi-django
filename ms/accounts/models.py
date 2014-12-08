# coding: utf-8

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from .constant import COMPOUND, AREA

class Compound(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    street_address = models.CharField(max_length=500, null=True, blank=True, verbose_name=u'Street number')
    street_name = models.CharField(max_length=500, null=True, blank=True)
    cross_street = models.CharField(max_length=500, null=True, blank=True)
    district = models.IntegerField(choices=AREA, null=True, blank=True, verbose_name=u'Area')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Ayi(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    pic = models.ImageField(upload_to='ayi/image/', null=True, blank=True, verbose_name='Ayi Photo')
    id_num = models.IntegerField(null=True, blank=True, verbose_name='ID card number')
    street_num = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=300, null=True, blank=True)
    area = models.IntegerField(choices=AREA, null=True, blank=True)
    mobile = models.BigIntegerField(validators=[MinValueValidator(10000000000)], verbose_name='Phone', null=True, blank=True)
    home = models.CharField(max_length=300, null=True, blank=True, verbose_name='Home Town')
    work_place = models.CharField(max_length=300, null=True, blank=True, verbose_name='Work Place')
    rate = models.IntegerField(null=True, blank=True, verbose_name='Rate')
    notes = models.TextField(null=True, blank=True, verbose_name=u'Notes')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('Customer'),
                                related_name='my_profile')
    mobile = models.BigIntegerField(validators=[MinValueValidator(10000000000)])
    street = models.CharField(max_length=300)
    compound = models.ForeignKey(Compound, null=True, blank=True)
    area = models.IntegerField(choices=AREA, null=True, blank=True)
    cross = models.CharField(max_length=300)
    street_num = models.CharField(max_length=100)
    bldg_num = models.CharField(max_length=100, null=True, blank=True)
    apt_num = models.CharField(max_length=100, null=True, blank=True)
    revenue = models.IntegerField(null=True, blank=True, verbose_name='Total Revenue')
    balance = models.IntegerField(null=True, blank=True, verbose_name='Balance')
    
    
    class Meta:
        verbose_name = 'All Customer'

    def __unicode__(self):
        return self.user.username
        
    def get_absolute_url(self):
        return reverse('userena_profile_edit', args=[str(self.user.username)])
