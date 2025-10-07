from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]