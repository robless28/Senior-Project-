from rest_framework import viewsets
from cases.models import Case
from documents.models import Document
from .serializers import CaseSerializer, DocumentSerializer

class CaseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing case instances.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer