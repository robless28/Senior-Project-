from django.http import HttpResponse
from django.urls import path
from .views import hello_clients

urlpatterns = [ path("", hello_clients, name = "clients-home")]