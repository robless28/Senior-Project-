from django.contrib import admin
from .models import Case

# This makes the Case model visible on the admin site.
admin.site.register(Case)