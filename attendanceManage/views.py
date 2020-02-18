from .models import attendanceManage,labourWorkTime
from rest_framework.views import APIView
from .serializers import attendanceSerializer,labourerworkTimeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shift.models import shift
from shift.serializers import shiftInfoSerializer
from datetime import datetime,timedelta,time
import json
from sitemanage.models import SiteManage
from sitemanage.serializers import SiteManageSerializer

class attendanceViews(APIView):

    def get(self,request):
        data = attendanceManage.objects.all()
        serialized = attendanceSerializer(data,many=True)
        return Response(serialized.data)

    def post(self,request):
        recivedata = recivedata.data
        serialized = attendanceSerializer(data=recivedata)
        if serialized.is_valid():
            attendaceRes = serialized.save()
            print("print attence response",attendaceRes)
            attendanceRes = {"status","attendace added suceefully"}
            return Response(attendaceRes)






@api_view(["POST"])
def checkin(request):
    data = request.data
    labourerid = data["labourerid"]
    siteid = data["siteid"]
    timeobj = data["time"]
    date  =  data["date"]
    siteobj = SiteManage.objects.filter(site_id=siteid)
    site = SiteManageSerializer(siteobj,many=True)
    start_time = str(site.data[0]["start_time"])
    print("starttime...........,,",start_time)
    shifttime = datetime.strptime(start_time,'%H:%M:%S').time()
    print("timeobj.......",timeobj)
    shiftid = "shift001"
    # intime = datetime.strptime("06:00:00",'%H:%M:%S') 
    intime = datetime.strptime(str(timeobj),'%H:%M:%S').time()
    print("shifttime",shifttime,"...........",timeobj)

    if intime < shifttime:
        check = labourWorkTime(labourerid=labourerid, siteid = siteid, date = date, intime =shifttime, shiftid = shiftid)
        check.save()
    else:
        check = labourWorkTime(labourerid=labourerid, siteid = siteid, date = date,intime =intime, shiftid = shiftid)
        check.save()        

    return Response("sucess")



@api_view(["POST"])
def checkout(request):
    data = request.data
    labourerid = data["labourerid"]
    siteid = data["siteid"]
    date = data["date"]
    outt = data["time"]

    siteobj = SiteManage.objects.filter(site_id=siteid)
    site = SiteManageSerializer(siteobj,many=True)
    end_time = str(site.data[0]["end_time"])
    buff_time = str(site.data[0]["end_buffer"])    

    outtime = datetime.strptime(outt,'%H:%M:%S')
    # closetime = datetime.strptime("18:30:00",'%H:%M:%S')
    closetime = datetime.strptime(str(end_time),'%H:%M:%S')
    # bufftime = datetime.strptime("19:00:00",'%H:%M:%S')
    bufftime = datetime.strptime(str(buff_time),'%H:%M:%S')

    if outtime.time() > closetime.time() and outtime.time() < bufftime.time():
        print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 1 ")
        checkin = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        intime = (labourerworkTimeSerializer(checkin,many=True).data)[0]["intime"]
        print("intime",intime)
        workhour = outtime.hour - datetime.strptime(intime,'%H:%M:%S').hour
        workminute = outtime.minute - datetime.strptime(intime,'%H:%M:%S').minute
        wotktime = datetime.strptime((str(workhour)+":"+str(workminute)+":"+"00"),'%H:%M:%S')
        print("workour.............",workhour,".........",workminute)
        data = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        data.update(outtime=closetime.time(),workhours=wotktime,othours="00:00:00",otstatus=False)        

    elif outtime.time()<closetime.time():
        print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 2 ")
        checkin = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        print("..................",(labourerworkTimeSerializer(checkin,many=True).data)[0])
        intime = (labourerworkTimeSerializer(checkin,many=True).data)[0]["intime"]
        print("intime",intime)
        workhour = outtime.hour - datetime.strptime(intime,'%H:%M:%S').hour
        if datetime.strptime(intime,'%H:%M:%S').minute < outtime.minute:
            workminute = outtime.minute - datetime.strptime(intime,'%H:%M:%S').minute
        workminute ="00"
        wotktime = datetime.strptime((str(workhour)+":"+str(workminute)+":"+"00"),'%H:%M:%S')        
        data = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        data.update(outtime=outtime.time(),workhours=wotktime,othours="00:00:00",otstatus=False) 

    else:      
        print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 3 ")
        checkin = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        intime = (labourerworkTimeSerializer(checkin,many=True).data)[0]["intime"]
        print("intime",intime)
        workhour = closetime.hour - datetime.strptime(intime,'%H:%M:%S').hour
        workminute = closetime.minute - datetime.strptime(intime,'%H:%M:%S').minute
        wotktime = datetime.strptime((str(workhour)+":"+str(workminute)+":"+"00"),'%H:%M:%S')        
        hours = outtime.hour-closetime.hour
        if closetime.minute > outtime.minute:
            minutes = outtime.minute-closetime.minute
        minutes ="00"
        print("....hour...minute",hours,minutes)
        otTime = datetime.strptime((str(hours)+":"+str(minutes)+":"+"00"),'%H:%M:%S')
        data = labourWorkTime.objects.filter(labourerid=labourerid,date=date)
        data.update(outtime=outtime.time(),workhours=wotktime,othours=otTime,otstatus=False)         

    return Response("sucess")






@api_view(['GET'])
def allAttendance(request):
    recdata = request.data
    attendance = labourWorkTime.objects.filter(siteid = "site005558")
    retdict = labourerworkTimeSerializer(attendance,many=True).data
    dates = ["2020-02-15","2020-07-02","2020-07-03"]
    print(".............",len(retdict))
    ls = []
    tupl = ()
    cnt = 0
    totaldict = {}
    for cnt in range(len(retdict)):
        print(".......",retdict[cnt]["labourerid"])
        labourerid = retdict[cnt]["labourerid"]
        dbft = dbfetch(labourerid,dates)
        ls.append(labourerid)
        ls.append(dbft)
    lt = []       
    lt.append(ls)
    return Response(lt)

def dbfetch(labourerid,dates):
    dbl = []
    for date in dates:
        print("dates0...........",date)
        lab = labourWorkTime.objects.filter(labourerid =labourerid,date=date)
        data = (labourerworkTimeSerializer(lab,many=True).data)[0]
        print("data.................................",data["workhours"])
        dicts = { "date":date,"workhour": data["workhours"],"OThour":data["othours"]}
        print("rec.....////////////..........",dicts)
        dbl.append(dicts)
        
    return dbl


@api_view(['GET'])
def personAttendance(request):
    recdata = request.data
    ls = []
    rec = []
    labourerid ="lab056522007"
    lab = labourWorkTime.objects.filter(labourerid =labourerid)
    dbdata = (labourerworkTimeSerializer(lab,many=True).data)
    print(".................",len(dbdata))
    for cnt in range(len(dbdata)):
        dicts = { "date":dbdata[cnt]["date"],"workhour": dbdata[cnt]["workhours"],"OThour":dbdata[cnt]["othours"]}
        print("./////////////////////...,,,0000",dicts)
        rec.append(dicts)
    ls.append(labourerid)
    ls.append(rec)

    return Response(ls)
