from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path('clientDashboard/', views.clientDashboard_view, name='clientDashboard'),

    path('clientProfilePage/', views.clientProfilePage_view, name='clientProfilePage'),
    

]