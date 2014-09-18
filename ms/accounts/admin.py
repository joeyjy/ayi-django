from django.contrib import admin                                                                                                            
from django.utils.translation import ugettext_lazy as _
 
from .models import *

class MyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'mobile', 'compound', 'get_join')
    search_fields = ('user__username', 'user__email', )
    ordering = ('user__username', )
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

for cls in [Compound, Ayi]:
    admin.site.register(cls)
