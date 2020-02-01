from django.urls import path
from .views import labourerInfoView


urlpatterns = [
    path('labourer',labourerInfoView.as_view())
]