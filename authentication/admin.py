from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(customuser)
class CustomUserAdmin(admin.ModelAdmin):
    pass