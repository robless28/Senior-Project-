from django.contrib import admin
from .models import ClientProfile

# This makes the ClientProfile model visible on the admin site
admin.site.register(ClientProfile)