from django.shortcuts import render
from django.http import HttpResponse

def clientDashboard_view(request):
    # This view simply renders the clientDashboard.html template
    return render(request, 'clients/clientDashboard.html')

def clientProfilePage_view(request):
    # This view simply renders the clientProfilePage.html template
    return render(request, 'clients/clientProfilePage.html')