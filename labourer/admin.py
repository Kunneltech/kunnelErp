from django.contrib import admin
from labourer.models import bankAccount_info,personal_info,identity_info,employeement_info
# Register your models here.
admin.site.register(personal_info)
admin.site.register(employeement_info)
admin.site.register(identity_info)
admin.site.register(bankAccount_info)