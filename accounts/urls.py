from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('registration/', views.registration_view, name='registration'),
]