from .models import account,accountinfo
from rest_framework.views import APIView
from .serializers import accountInfoSerializer,accountSerializer
from rest_framework.response import Response



class accountViews(APIView):

    def get(self,request):
        data = account.objects.all()
        serialized = accountSerializer(data,many=True)
        return Response(serialized.data)

    def post(self,request):
        recivedata = request.data
        serialized = accountSerializer(data=recivedata)
        if serialized.is_valid():
            accountRes = serialized.save()
            print("accounting status",accountRes)
            response = {"status":"account details added sucessfully"}
            return Response(response)

class accountInfoViews(APIView):
    def get(self,request):
        data = accountinfo.objects.all()
        serialized = accountInfoSerializer(data,many=True)
        return Response(serialized.data)  

    def post(self,request):
        recivedata = request.data
        serialized = accountInfoSerializer(data=recivedata)
        if serialized.is_valid():
            accountInfoRes = serialized.save()
            print("accounting status",accountInfoRes)
            response = {"status":"account details added sucessfully"}
            return Response(response)


        
        