from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from cases.models import Case

def clientProfilePage_view(request):
    # This view simply renders the clientProfilePage.html template
    return render(request, 'clients/client_profile.html')

def client_registration_view(request):
    return render(request, 'clients/clientRegistration.html')

def client_login_view(request):
    return render(request, 'clients/clientLogin.html')

@login_required
def clientDashboard(request):
    return render(request, 'clients/clientDashboard.html')
