from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('registration/', views.registration_view, name='registration'),
    path('', views.home_view, name='home'),
    path('register/attorney/', views.attorney_registration_view, name='attorney_registration'),


]