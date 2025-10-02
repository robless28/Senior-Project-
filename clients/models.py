from django.db import models
from django.core.validators import RegexValidator

class Clients(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
 
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-format phone number before saving
        if self.phone:
            digits = ''.join(filter(str.isdigit, self.phone))  # keep only numbers
            if len(digits) == 10:  # format as (XXX) XXX-XXXX
                self.phone = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
            elif len(digits) == 11 and digits.startswith("1"):  # US country code
                self.phone = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
            else:
                self.phone = f"+{digits}"  # fallback for international
        super().save(*args, **kwargs)
