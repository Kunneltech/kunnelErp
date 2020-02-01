from django.urls import path
from .views import projectView,siteView


urlpatterns = [
    path('site',siteView.as_view()),
    path('project',projectView.as_view())
]