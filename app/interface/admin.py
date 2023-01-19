from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser


class CustomAdmin(UserAdmin):
    list_display = (
        "username", "first_name", "token"
    )

    fieldsets = (
        ("reg", {'fields': ('username',  'password')}),
        ('Personal info', {'fields': ('first_name', 'token', "chat_id")})
    )

    readonly_fields = (['token', 'chat_id'])


admin.site.register(CustomUser, CustomAdmin)
