from .models import bankAccount_info,employeement_info,identity_info,personal_info
from rest_framework import serializers

class personalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = personal_info
        fields = '__all__'

class employeementInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeement_info
        fields = '__all__'

class identyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = identity_info
        fields = '__all__'
        
class bankaccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = bankAccount_info
        fields = '__all__'
