from django.contrib import admin
from .models import Away, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Away)
admin.site.register(User, UserAdmin)
