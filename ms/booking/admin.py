from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from booking.models import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booker', 'status', 'get_compound', 'clean_ayi', 'bedroom',)
    search_fields = ('booker__username', 'booker__email', )
    ordering = ('booker__username', )
    #list_filter = ['date_created']
    def get_compound(self, obj):
        return obj.booker.my_profile.compound
    get_compound.short_description = 'Compound'
    get_compound.admin_order_field = 'booker__my_profile__compound'

admin.site.register(Booking, BookingAdmin)
#for cls in [Booking, BookingAdmin]:
#    admin.site.register(cls)
