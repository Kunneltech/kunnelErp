from rest_framework import serializers
from sitemanage.models import SiteManage




class SiteManageSerializer(serializers.ModelSerializer):

	class Meta:
		model = SiteManage
		fields = '__all__'

class SiteManageCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = SiteManage
		fields = '__all__'