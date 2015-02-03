from django.contrib import admin                                                                                                            
from django.utils.translation import ugettext_lazy as _
 
from .models import *

class AyiAdmin(admin.ModelAdmin):
    fields = ('name', 'id_num', 'street_num', 'street', 'area', 'mobile', 'home', 'work_place', 'rate', 'notes', 'pic', 'admin_image',)
    list_display = ('name', 'area', 'mobile', 'rate', 'home', 'work_place',)
    #readonly_fields = ('admin_image',)
    list_filter = ('area',)
    class Media:
        js = ['js/list_filter_collapse.js']

class MyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_join', 'compound', 'area', 'get_email', 'mobile', 'revenue', 'balance')
    search_fields = ('user__username', 'user__email', )
    ordering = ('user__username', )
    list_filter = ('area',)
    class Media:
        js = ['js/list_filter_collapse.js']
    #list_filter = ['date_created']
    def get_email(self, obj):
        return obj.user.email
    def get_join(self, obj):
        return obj.user.date_joined
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'
    get_join.short_description = 'Join Date'
    get_join.admin_order_field = 'user__date_joined'

admin.site.unregister(MyProfile)
admin.site.register(MyProfile, MyProfileAdmin)
admin.site.register(Ayi, AyiAdmin)

for cls in [Compound,]:
    admin.site.register(cls)
