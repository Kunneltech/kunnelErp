from .models import account,accountinfo
from rest_framework import serializers

class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'

class accountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountinfo
        fields = '__all__'

