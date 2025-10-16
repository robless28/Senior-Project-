from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

 # Manages users, registration, login/logout, and user roles (like distinguishing between an "Attorney" and a "Client"). 
class Role(models.Model):
    # The name of the role (e.g., 'ATTORNEY', 'CLIENT', 'ADMIN')
    name = models.CharField(max_length=50, unique=True)
    # A short, descriptive display name
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # username is still required under the hood

    # Custom Fields
    roles = models.ManyToManyField(
        'accounts.Role',  # Point this to your new Role model
        related_name='users',
        blank=True
    )
    
    phone_regex = RegexValidator( # Regex validator ensures phone numbers follow a patter
        regex=r'^\+?1?\d{9,15}$', # start of string, optional + sign, optional leading 1 (US code), 9-15 digits, $ end of string
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed." # error if validation fails
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) # applies regex validation, field is optional in forms, field can store null in database
    address = models.TextField(blank=True, null=True) # for longer text, optional can be left empty

    def __str__(self):
            return self.email
    
    def save(self, *args, **kwargs): #overrides built-in save method
        # Auto-format phone number before saving
        if self.phone: # if client has entered phone number, process before saving
            digits = ''.join(filter(str.isdigit, self.phone))  # keep only numbers
            if len(digits) == 10:  # format as (XXX) XXX-XXXX
                self.phone = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
            elif len(digits) == 11 and digits.startswith("1"):  # US country code
                self.phone = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
            else:
                self.phone = f"+{digits}"  # fallback for international
        super().save(*args, **kwargs) # calls original save method, without nothing saves

# (python manage.py makemigrations) - looks at your models and prepares instructions
# (pyhton manage.py migrate) - applies instructions to actual database (SQLite in Django)

# Django comes with an ORM (Object-Relational Mapper) so you don't need to write raw SQL, just use python code
