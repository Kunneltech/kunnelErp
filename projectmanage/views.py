from rest_framework.response import Response
from .models import project, site
from .serializers import projectSerializer,siteSerializer
from rest_framework.views import APIView




class projectView(APIView):
    def get(self,request):
        dbdata = project.objects.all()
        projectserilized = projectSerializer(dbdata,many=True)      
        return Response(responsedict)        


    def post(self,request):
        recivedata = request.data
        serialized = projectSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"project added sucessfully created sucessfully"}
            return Response(response)   


class siteView(APIView):
    def get(self,request):
        sitedbdata = project.objects.all()
        siteserilized = siteSerializer(sitedbdata,many=True)     
        return Response(siteserilized.data)        


    def post(self,request):
        recivedata = request.data
        serialized = siteSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"siteinfo added sucessfully created sucessfully"}
            return Response(response)   