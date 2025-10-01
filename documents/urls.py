from django.http import HttpResponse
from django.urls import path
from .views import hello_documents


urlpatterns = [ path("", hello_documents, name="documents-home")]
