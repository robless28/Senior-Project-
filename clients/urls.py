from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('clientDashboard/', views.clientDashboard_view, name='clientDashboard'),

    path('clientProfilePage/', views.clientProfilePage_view, name='clientProfilePage'),
    

]