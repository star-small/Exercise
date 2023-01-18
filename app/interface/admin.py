from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser


class CustomAdmin(UserAdmin):
    list_display = (
        "username", "first_name", "token"
    )
    fieldsets = (
        ("reg", {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'token')})
    )
    readonly_fields = (['token'])


admin.site.register(CustomUser, CustomAdmin)
