from rest_framework import serializers
from .models import SiteManage

class siteManageSerializers(serializers.ModelSerializers):
    class Meta:
        model = SiteManage
        fields = '__all__'