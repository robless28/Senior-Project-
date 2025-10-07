from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'role']

admin.site.register(CustomUser, CustomUserAdmin)