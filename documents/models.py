from django.db import models
from django.conf import settings
from cases.models import Case

class Document(models.Model):
    file = models.FileField(upload_to='case_documents/')
    description = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)

    # --- Relationships ---
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.file.name