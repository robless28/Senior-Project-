from rest_framework import serializers
from cases.models import Case
from documents.models import Document
from dj_rest_auth.registration.serializers import RegisterSerializer


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        # These are the fields that will be included in the API response
        fields = ['id', 'case_name', 'case_number', 'description', 'status', 'date_opened', 'attorney', 'client']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'description', 'upload_date', 'case', 'uploaded_by']

class CustomRegisterSerializer(RegisterSerializer):
    # We override the default save method
    def save(self, request):
        # Call the parent class's save method to create the user
        user = super().save(request)
        # Set the user's role to CLIENT
        user.role = 'CLIENT'
        user.save()
        return user