from django.contrib import admin
from .models import *

# Register your models here.

class PersonalMenuAdmin(admin.ModelAdmin):
    list_display = ["user_id", "dish"]

class DishItemAdmin(admin.ModelAdmin):
    list_display = ["item", "dish"]
    
class GroceryCategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]
    
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ["item", "category"]

class GroceryListAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "item", "completed", "date"]
    
class GroceryListNameAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "name"]
    



admin.site.register(PersonalMenu, PersonalMenuAdmin)
admin.site.register(DishItem, DishItemAdmin)
admin.site.register(GroceryCategory, GroceryCategoryAdmin)
admin.site.register(GroceryItem, GroceryItemAdmin)
admin.site.register(GroceryList, GroceryListAdmin)
admin.site.register(GroceryListName, GroceryListNameAdmin)
admin.site.register(UserPost)
admin.site.register(UserComments)

