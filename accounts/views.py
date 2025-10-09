from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    # This view simply renders the login.html template
    return render(request, 'accounts/login.html')

def registration_view(request):
    # This view simply renders the registration.html template
    return render(request, 'accounts/registration.html')

@login_required
def dashboard_view(request):
    if request.user.role == 'ATTORNEY':
        # Show the attorney's dashboard
        return render(request, 'accounts/attorney_dashboard.html')
    elif request.user.role == 'CLIENT':
        # Show the client's dashboard
        return render(request, 'clients/clientDashboard.html')
    else:
        # If user has no role, send them back to login
        return redirect('login')