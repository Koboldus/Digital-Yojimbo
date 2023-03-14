from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import L5RUser

admin.site.register(L5RUser, UserAdmin)
