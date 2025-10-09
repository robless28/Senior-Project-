from django.db import models
from django.conf import settings

class ClientProfile(models.Model):
    # This creates a strict one-to-one link to your main user model.
    # If a user is deleted, their profile is deleted too (on_delete=models.CASCADE).
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    # --- Add only client-specific fields here ---
    company_name = models.CharField(max_length=255, blank=True)
    preferred_contact_method = models.CharField(
        max_length=10,
        choices=[('EMAIL', 'Email'), ('PHONE', 'Phone')],
        default='EMAIL'
    )
    onboarding_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile for {self.user.email}"