from django.contrib import admin
from .models import *

# Register your models here.

class PersonalMenuAdmin(admin.ModelAdmin):
    list_display = ["user_id", "dish"]

class DishItemAdmin(admin.ModelAdmin):
    list_display = ["item", "dish"]

admin.site.register(PersonalMenu, PersonalMenuAdmin)
admin.site.register(DishItem, DishItemAdmin)