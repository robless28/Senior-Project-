from django.shortcuts import render
from django.http import HttpResponse


def hello_cases(request):
    return HttpResponse("Cases says hello ")
