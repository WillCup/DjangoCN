from django.contrib import admin
from .models import User


class UserCenterAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_login', 'date_joined']


admin.site.register(User, UserCenterAdmin)
