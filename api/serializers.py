from rest_framework import serializers
from cases.models import Case
from documents.models import Document
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model



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
    # 1. Add the fields you want to collect and validate
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=150)
    
    # 2. Add the password confirmation field (standard dj-rest-auth uses 'password2' or 'password_confirm', check documentation if this fails)
    # The base RegisterSerializer should handle the password and password2 fields if you are using allauth's default forms.
    # However, explicitly defining them is necessary if you override the save method to ensure they are validated.
    
    # We override the default save method
    def save(self, request):
        # 3. Retrieve the extra fields from validated data
        first_name = self.validated_data.get('first_name', '')
        last_name = self.validated_data.get('last_name', '')
        
        # Call the parent class's save method to create the user
        # This will handle email, password, and password2/confirm
        user = super().save(request)
        
        # 4. Save the extra fields to the user model
        user.first_name = first_name
        user.last_name = last_name
        
        # Set the user's role to CLIENT (already there)
        user.role = 'CLIENT'
        
        user.save()
        return user
    
class AttorneyRegisterSerializer(RegisterSerializer):
    # Add fields to validate and process
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=150)
    
    # *** FIX 1: Add the username field, make it read-only, and provide a default***
    username = serializers.CharField(required=True, max_length=150)
    
    def validate_username(self, value):
        # Override the validation to allow it to pass, 
        # as we will override it in the save method.
        return value

    def save(self, request):
        # 1. Manually set the username to the email before calling super().save()
        self.validated_data['username'] = self.validated_data['email']
        
        # ... (rest of the save method remains the same) ...
        # 2. Call parent to handle core user creation (email, password, password2, and now username)
        user = super().save(request)

        # 3. Save extra fields
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')

        # 4. Set the role
        user.role = 'ATTORNEY'
        
        user.save()
        return user    # Add fields to validate and process
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=150)
    
    # *** ADD THIS FIELD ***
    # This field is required by the base serializer for password confirmation.
    # It will automatically be validated against 'password'.
    password2 = serializers.CharField(
        style={'input_type': 'password'}, label='Confirm Password', write_only=True
    )

    def save(self, request):
        # ... (rest of the save method is correct)
        
        # 1. Retrieve the extra fields from validated data
        first_name = self.validated_data.get('first_name', '')
        last_name = self.validated_data.get('last_name', '')

        # 2. Call parent to handle core user creation (email, password, and now password2)
        user = super().save(request)

        # 3. Save extra fields
        user.first_name = first_name
        user.last_name = last_name

        # 4. Set the role
        user.role = 'ATTORNEY'
        
        user.save()
        return user
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'role')
