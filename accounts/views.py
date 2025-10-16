from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cases.models import Case


def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    # This view simply renders the login.html template
    return render(request, 'accounts/login.html')

def registration_view(request):
    # This view simply renders the registration.html template
    return render(request, 'accounts/registration.html')

def attorney_registration_view(request):
    return render(request, 'accounts/attorney_registration.html')


def attorney_profile_view(request):
    return render(request, 'accounts/attorney_profile.html')

@login_required
def attorney_dashboard(request):
    return render(request, 'accounts/attorney_dashboard.html')


@login_required
def dashboard_view(request):
     if request.user.role == 'ATTORNEY':
        # Get all cases where the attorney is the currently logged-in user
        cases = Case.objects.filter(attorney=request.user)
        context = {'cases': cases}
        return render(request, 'accounts/attorney_dashboard.html', context)
     
     elif request.user.role == 'CLIENT':
        # Get all cases where the client is the currently logged-in user
        cases = Case.objects.filter(client=request.user)
        context = {'cases': cases}
        return render(request, 'clients/clientDashboard.html', context)

     else:
        return redirect('accounts:login')