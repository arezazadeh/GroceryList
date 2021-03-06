from django.contrib import admin
from .models import *

# Register your models here.

class PersonalMenuAdmin(admin.ModelAdmin):
    list_display = ["user_id", "username", "dish"]

class DishItemAdmin(admin.ModelAdmin):
    list_display = ["item", "dish"]
    
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "item", "completed", "date"]
    
class GroceryListAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "username", "name"]
    

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "user_id"]


class UserPostAdmin(admin.ModelAdmin):
    list_display = ["id", "post"]
    
class LikeAdmin(admin.ModelAdmin):
    list_display = ["post", "user_name", "date"]
    

class DisLikeAdmin(admin.ModelAdmin):
    list_display = ["post", "user_name", "date"]

admin.site.register(PersonalMenu, PersonalMenuAdmin)
admin.site.register(DishItem, DishItemAdmin)
admin.site.register(GroceryItem, GroceryItemAdmin)
admin.site.register(GroceryList, GroceryListAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(UserComments)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(DisLike, DisLikeAdmin)

