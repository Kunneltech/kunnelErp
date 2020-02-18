from django.urls import path
from .views import  (personAttendance,allAttendance,checkin,attendanceViews,checkout)


urlpatterns =[
    path('attendance',attendanceViews.as_view()),
    path('singleperson',personAttendance),
    path('allAttendance',allAttendance),
    path('checkin',checkin),
    path('checkout',checkout)
]