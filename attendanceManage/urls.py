from django.urls import path
from .views import  (attendanceViews)


urlpatterns =[
    path('attendance',attendanceViews.as_view())
]