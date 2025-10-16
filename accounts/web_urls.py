from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('registration/attorney/', views.attorney_registration_view, name='attorney_registration'),
    path('attorney_dashboard/', views.attorney_dashboard, name='attorney_dashboard'),
    path('attorney_profile/', views.attorney_profile_view, name='attorney_profile'),
]