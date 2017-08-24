from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentsPlate)
class StudentsPlateAdmin(admin.ModelAdmin):
    pass


@admin.register(ExecutivePlate)
class ExecutivePlateAdmin(admin.ModelAdmin):
    pass


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    pass
