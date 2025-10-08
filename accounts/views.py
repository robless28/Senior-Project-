from django.shortcuts import render
from django.http import HttpResponse


def login_view(request):
    # This view simply renders the login.html template
    return render(request, 'accounts/login.html')

def registration_view(request):
    # This view simply renders the registration.html template
    return render(request, 'accounts/registration.html')