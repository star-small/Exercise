from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser


class CustomAdmin(UserAdmin):
    list_display = (
        "username", "first_name", "token"
    )


admin.site.register(CustomUser, CustomAdmin)
