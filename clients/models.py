from django.db import models
from django.core.validators import RegexValidator

# Create and define a Model (Python class) which represents a table
# in the database
class Client(models.Model):
    # each attribute represents a column in the Clients table
    # automatically gives primary key (id) unless specified otherwise
    firstname = models.CharField(max_length=255) # CharField is a text column with character limit
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True) # EmailField validates the format looks like an email
    # unique = true -> prevents duplicate emails in database
 
    phone_regex = RegexValidator( # Regex validator ensures phone numbers follow a patter
        regex=r'^\+?1?\d{9,15}$', # start of string, optional + sign, optional leading 1 (US code), 9-15 digits, $ end of string
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed." # error if validation fails
    )
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True, null=True)
    # applies regex validation, field is optional in forms, field can store null in database

    address = models.TextField(blank=True, null=True) # for longer text
    # optional can be left empty

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

"""
For example
# Add a new client
client = Client.objects.create(
    firstname="Maria",
    lastname="Gonzalez",
    email="maria@example.com",
    phone="123-456-7890",
    address="123 Main St"
)

# Query clients
all_clients = Client.objects.all()
specific_client = Client.objects.get(id=1)

"""