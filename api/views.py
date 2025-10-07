from rest_framework import viewsets
from cases.models import Case
from .serializers import CaseSerializer

class CaseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing case instances.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer