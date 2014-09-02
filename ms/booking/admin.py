from django.contrib import admin
from booking.models import *

for cls in [Booking,]:
    admin.site.register(cls)
