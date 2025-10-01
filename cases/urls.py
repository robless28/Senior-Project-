from django.http import HttpResponse
from django.urls import path
from .views import hello_cases


urlpatterns = [ path("", hello_cases, name="cases-home") ]