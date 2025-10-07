from django.contrib import admin
from .models import Document

# This makes the Document model visible on the admin site.
admin.site.register(Document)