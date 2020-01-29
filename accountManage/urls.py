from django.urls import path
from .views import  (accountInfoViews,accountViews)


urlpatterns =[
    path('account',accountViews.as_view()),
    path('accountinfo',accountInfoViews.as_view())
]