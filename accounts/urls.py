from django.http import HttpResponse
from django.urls import path
from .views import hello_accounts


urlpatterns = [ path("", hello_accounts, name="accounts-home") ]