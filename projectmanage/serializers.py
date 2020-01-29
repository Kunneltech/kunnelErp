from .models import project,site
from rest_framework import serializers

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class siteSerializer(serializers.ModelSerializer):
    class Meta:
        model = site
        fields = '__all__'
