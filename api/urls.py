from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, DocumentViewSet 

router = DefaultRouter()
router.register(r'cases', CaseViewSet, basename='case')
router.register(r'documents', DocumentViewSet, basename='document') # <-- ADD THIS LINE

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]