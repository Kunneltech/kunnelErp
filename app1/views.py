from django.shortcuts import render
from .models import Staff,SubContractor,SiteManagement,customUser
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User=get_user_model()
from app1.serializers import staffSerializer,sitemanageSerilizers,subContractSerilizer,userSerilizer
# from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json
# Create your views here.
class userViews(APIView):

    def get(self,request):
        user = User.objects.all()
        print("......recive data",user)
        serilized = userSerilizer(user,many=True)
        print("serilized,............",serilized)
        print("serilized,........data....",serilized.data)

        return Response(serilized.data)

    def post(self,request):
        # import pdb;pdb.set_trace()
        reciveData = request.data
        print("......................",reciveData)
        print("......................username.............",reciveData['username'])
        serilized = userSerilizer(data=reciveData)
        print("serialized data...............",serilized)
        if serilized.is_valid():
            user = serilized.save()
            print("id printing...........",user)
            token = Token.objects.create(user=user)
            print("token",token)
            # data["response"]="sucess"
            # data["token"]= str(toekn)
            response = {"satus":"user created sucessfully"}
            return Response(response)


class staffViews(APIView):

    def get(self,request):
        staff = Staff.objects.all()
        print("......recive data",staff)
        serilized = staffSerializer(staff,many=True)
        print("serilized,............",serilized)
        print("serilized,........data....",serilized.data)
        return Response(serilized.data)

    def post(self,request):
        reciveData = request.data
        print("......................",reciveData)
        serilized = staffSerializer(data=reciveData)
        print("serialized data...............",serilized)
        if serilized.is_valid():
            staff = serilized.save()
            print("resa,,,",staff)
            response = {"satus":"staff created sucessfully"}
        return Response(response)


class subContractViews(APIView):

    def get(self,request):
        contract = SubContractor.objects.all()
        print("......recive data",contract)
        serilized =subContractSerilizer(contract,many=True)
        print("serilized,............",serilized)
        print("serilized,........data....",serilized.data)
        return Response(serilized.data)

    def post(self,request):
        reciveData = request.data
        print("......................",reciveData)
        serilized = subContractSerilizer(data=reciveData)
        print("serialized data...............",serilized)
        if serilized.is_valid():
            user = serilized.save()
            response = {"satus":"subcontract created sucessfully"}
        return Response(response)

class sitemanageViews(APIView):

    def get(self,request):
        site = SiteManagement.objects.all()
        print("......recive data",site)
        serilized =sitemanageSerilizers(site,many=True)
        print("serilized,............",serilized)
        print("serilized,........data....",serilized.data)
        return Response(serilized.data)

    def post(self,request):
        reciveData = request.data
        print("......................",reciveData)
        serilized = sitemanageSerilizers(data=reciveData)
        print("serialized data...............",serilized)
        if serilized.is_valid():
            user = serilized.save()
            response = {"satus":"site added sucessfully"}
        return Response(response)        



class loginView(APIView):
    
    def post(self,request):
        reciveData = request.data
        # print("recive data",reciveData)
        user = authenticate(username=reciveData["username"],password=reciveData["password"])
        # user1 = User.objects.filter(username=user)
        # print(",,,,,,,user1",user1)
        print("user,,,,,,",user)
        if user == None:
            print("if part is working")
            token =Token.objects.create(user=user)
        else:
            print("else part working")
            token = Token.objects.filter(user=user).first()
            # print(";;;;;;;",token.key)
            data = { "status":"login sucessfully","token":str(token.key)}
            print("data",data)
        return Response(data)



        
    
