from rest_framework import serializers
from cases.models import Case

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        # These are the fields that will be included in the API response
        fields = ['id', 'case_name', 'case_number', 'description', 'status', 'date_opened', 'attorney', 'client']