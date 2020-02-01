from django.urls import path
from .views import labourerclassView


urlpatterns = [
    path('labourerclass',labourerclassView.as_view())
]