from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import ClientProfile

# This function will run every time a User model is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_client_profile(sender, instance, created, **kwargs):
    # If a new user was created AND their role is 'CLIENT'
    if created and instance.role == 'CLIENT':
        # Create a new ClientProfile and link it to that user
        ClientProfile.objects.create(user=instance)