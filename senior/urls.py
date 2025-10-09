"""
URL configuration for senior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse('This is the homePage')

urlpatterns = [
    # Frontend root
    path("", TemplateView.as_view(template_name="index.html"), name="home"),

    # Admin
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include('accounts.urls')),          # 👈 includes registration/attorney/
    path('api/', include('clients.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/', include('api.urls')),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Other app routes
    path('cases/', include('cases.urls')),
    path('documents/', include('documents.urls')),
    path('clients/', include(('clients.urls', 'clients'), namespace='clients')),
    path('accounts/', include(('accounts.urls'), namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
