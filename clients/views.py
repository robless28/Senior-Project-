from django.shortcuts import render
from django.http import HttpResponse

def hello_clients(request):
    return HttpResponse("Clients says hello ")