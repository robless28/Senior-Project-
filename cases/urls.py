from django.http import HttpResponse
from django.urls import path
from .views import hello_cases
from . import views


urlpatterns = [
     path("cases/", views.hello_cases, name="cases/"),
     
     ]