from django.urls import path
from .views import paymentView


urlpatterns = [
    path('payment',paymentView.as_view())
]