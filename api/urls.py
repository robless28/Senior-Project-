from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, DocumentViewSet
from accounts.views import attorney_registration_view
from clients.views import client_registration_view

router = DefaultRouter()
router.register(r'cases', CaseViewSet, basename='case')
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.registration.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('registration/attorney/', attorney_registration_view, name='attorney_registration'),
    path('registration/client/', client_registration_view, name='clientRegistration')
]
