from rest_framework import serializers
from .models import customUser,Staff,SubContractor,SiteManagement

class userSerilizer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = '__all__'
    def create(self, validated_data):
            # user = User(email=validated_data['email'], username=validated_data['username'])
            user = super(userSerilizer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user


class staffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [  
                    'name',
                    'address',
                    'adaar',
                    'fatherName',
                    'department',
                    'BankAC' ,
                    'contact',
                    'bloodGroup',
                    'employeeCode',
                    'salaryStructure'
                    ]

class subContractSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SubContractor
        fields = [
                'category',
                'nameOfContractor',
                'nameOfEmployee',
                'GSTRegistration',
                'adhar'
                ]

class sitemanageSerilizers(serializers.ModelSerializer):
    class Meta:
        model = SiteManagement
        fields =[
                'name',
                'address',
                'clientName',
                'projectManager',
                'typeOFProject',
                'siteEngineer',
                'startDate',
                'endDate',
                'lunchTime',
                'startTime' ,
                'salaryStructure',
                ]