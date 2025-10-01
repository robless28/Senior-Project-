from django.shortcuts import render
from django.http import HttpResponse


def hello_accounts(request):
    return HttpResponse("Accounts says hello ")
