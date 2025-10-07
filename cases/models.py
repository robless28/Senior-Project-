from django.db import models
from django.conf import settings

class Case(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('PENDING', 'Pending'),
    )

    case_name = models.CharField(max_length=255)
    case_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    date_opened = models.DateField(auto_now_add=True)

    # --- Relationships ---
    attorney = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cases_managed'
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cases_involved'
    )

    def __str__(self):
        return self.case_name