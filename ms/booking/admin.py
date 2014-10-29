from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from booking.models import *

class UserInline(admin.TabularInline):
    model = User

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booker', 'status', 'date_created', 'hour', 'clean_time', 'get_compound', 'get_area', 'clean_ayi', 'bedroom',)
    search_fields = ('booker__username', 'booker__email', )
    ordering = ('-date_created', )
    readonly_fields = ('get_name', 'get_mobile', 'get_email', 'get_compound', 'get_street_num', 'get_street', 'get_cross', 'get_area', 'get_bldg', 'get_apt')
    #list_filter = ['date_created']
    def get_name(self, obj):
        return obj.booker.get_full_name()
    def get_mobile(self, obj):
        return obj.booker.my_profile.mobile
    def get_email(self, obj):
        return obj.booker.email
    def get_compound(self, obj):
        return obj.booker.my_profile.compound
    def get_street_num(self, obj):
        return obj.booker.my_profile.street_num
    def get_street(self, obj):
        return obj.booker.my_profile.street
    def get_cross(self, obj):
        return obj.booker.my_profile.cross
    def get_area(self, obj):
        return obj.booker.my_profile.get_area_display()
    def get_bldg(self, obj):
        return obj.booker.my_profile.bldg_num
    def get_apt(self, obj):
        return obj.booker.my_profile.apt_num
    get_mobile.short_description = 'Mobile'
    get_mobile.admin_order_field = 'booker__my_profile__mobile'
    get_name.short_description = 'Full Name'
    get_name.admin_order_field = 'booker__get_full_name()'
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'booker__email'
    get_compound.short_description = 'Compound'
    get_compound.admin_order_field = 'booker__my_profile__get_compound_display()'
    get_street_num.short_description = 'Street num'
    get_street.short_description = 'Street name'
    get_cross.short_description = 'Cross street'
    get_area.short_description = 'Area'
    get_area.admin_order_field = 'booker__my_profile__get_area_display()'
    get_bldg.short_description = 'Building #'
    get_bldg.admin_order_field = 'booker__my_profile__get_bldg_display()'
    get_apt.short_description = 'Apartment #'
    get_apt.admin_order_field = 'booker__my_profile__get_apt_display()'

admin.site.register(Booking, BookingAdmin)
#for cls in [Booking, BookingAdmin]:
#    admin.site.register(cls)
