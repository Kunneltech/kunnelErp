from django.urls import path
from .views import shiftView


urlpatterns = [
    path('shift',shiftView.as_view())
]