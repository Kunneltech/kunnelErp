from django.urls import path
from .views import (SiteAPIView,addLabourerToSiteAPIView)


urlpatterns = [
    path('create/',SiteAPIView.as_view({'post':'post'})),
    path('sites/',SiteAPIView.as_view({'get':'list'})),
    path('sites/<int:pk>/',SiteAPIView.as_view({'get':'retrive'}),name='site_detail'),
    path('addlabourer/',addLabourerToSiteAPIView)
]

    # path('create/',SiteAPIView.as_view({'post':'post'})),
    # path('sites/',SiteAPIView.as_view({'get':'list'})),
    # path('sites/<int:pk>/',SiteAPIView.as_view({'get':'retrive'}),name='site_detail'),