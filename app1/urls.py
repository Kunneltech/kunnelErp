from django.urls import path
from .views import  (sitemanageViews,staffViews,subContractViews,userViews,loginView )


urlpatterns =[
    path('user',userViews.as_view()),
    path('staff',staffViews.as_view()),
    path('sitemanage',sitemanageViews.as_view()),
    path('subcontract',subContractViews.as_view()),
    path("login",loginView().as_view())
]