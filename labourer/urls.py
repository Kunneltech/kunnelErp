from django.urls import path
from .views import labourerView


urlpatterns = [
    path('labourer',labourerView.as_view())
]