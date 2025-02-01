from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'gender', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomerUser, CustomUserAdmin)