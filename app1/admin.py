from django.contrib import admin
from .models import  SubContractor,Staff,SiteManagement,customUser,customAdmin
# Register your models here.
admin.site.register(SubContractor)
admin.site.register(Staff)
admin.site.register(SiteManagement)
admin.site.register(customAdmin)
admin.site.register(customUser)