from rest_framework.views import APIView
from .models import bankAccount_info,personal_info,identity_info,employeement_info
from .serializers import bankaccountInfoSerializer,employeementInfoSerializer,identyInfoSerializer,personalInfoSerializer
from rest_framework.response import Response

class labourerInfoView(APIView):
    def get(self,request):
        personaldbdata  = personal_info.objects.all()
        bankdbdata      = bankAccount_info.objects.all()
        identitydbdata  = identity_info.objects.all()
        employeedbdata  = employeement_info.objects.all()

        personserialized    = personalInfoSerializer(personaldbdata,many=True)
        bankserialized      = bankaccountInfoSerializer(bankdbdata, many=True)
        identyserialized    = identyInfoSerializer(identitydbdata,many=True)
        employeeserialized  = employeementInfoSerializer(employeedbdata,many=True) 

        responseDict = {}
        responseDict["personaldata"] = [personserialized.data]
        responseDict["bankdata"]     = [bankserialized.data]
        responseDict["identitydata"] = [identyserialized.data]
        responseDict["employeedat"]  = [employeeserialized.data]

        return Response(responseDict)
    
    def post(self,request):
        recivedata = request.data
        personserialized    = personalInfoSerializer(data=recivedata)
        bankserialized      = bankaccountInfoSerializer(data=recivedata)
        identyserialized    = identyInfoSerializer(data=recivedata)
        employeeserialized  = employeementInfoSerializer(data=recivedata)
        
        if personserialized.is_valid() and bankserialized.is_valid() and identyserialized.is_valid() and employeeserialized.is_valid():
            personserialized.save()
            employeeserialized.save()
            identyserialized.save()
            bankserialized.save()
            response = {"satus":"labourer added sucessfully created sucessfully"}
            return Response(response)            