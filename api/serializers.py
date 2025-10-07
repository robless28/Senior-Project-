from rest_framework import serializers
from cases.models import Case
from documents.models import Document

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        # These are the fields that will be included in the API response
        fields = ['id', 'case_name', 'case_number', 'description', 'status', 'date_opened', 'attorney', 'client']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'description', 'upload_date', 'case', 'uploaded_by']
