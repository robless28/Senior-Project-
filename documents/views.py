from django.shortcuts import render
from django.http import HttpResponse



def hello_documents(request):
    return HttpResponse("Documents says hello ")
