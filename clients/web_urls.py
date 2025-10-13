from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'clients'

urlpatterns = [
    path('clientLogin/', views.client_login_view, name='clientLogin'),
    path('clientRegistration/', views.client_registration_view, name='clientRegistration'),
    path('clientProfilePage/', views.clientProfilePage_view, name='clientProfilePage'),
    path('clientDashboard/', views.clientDashboard, name='clientDashboard'),
]