from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from .constant import COMPOUND, AREA

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    mobile = models.BigIntegerField()
    street = models.CharField(max_length=300)
    compound = models.IntegerField(choices=COMPOUND, null=True, blank=True)
    area = models.IntegerField(choices=AREA, null=True, blank=True)
    cross = models.CharField(max_length=300)
    street_num = models.IntegerField()
    bldg_num = models.IntegerField(null=True, blank=True)
    apt_num = models.IntegerField(null=True, blank=True)
