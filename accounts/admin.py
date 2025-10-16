from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = (
        'email', 
        'first_name', 
        # REMOVE 'role' if you made the M2M change
        # ADD a custom method to display roles:
        'get_user_roles', 
        'is_staff'
    )

    def get_user_roles(self, obj):
        # Assumes your M2M field is named 'roles'
        return ", ".join([r.name for r in obj.roles.all()])
    get_user_roles.short_description = 'Roles'

admin.site.register(CustomUser, CustomUserAdmin)