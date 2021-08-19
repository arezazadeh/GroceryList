from django.contrib import admin
from django.urls import path, include
from requests import api
from . import views
from api.models import *

grocery_list_name_api = GroceryListNameResource()
grocery_list_api = GroceryListResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('grocery/', include('grocery.urls')),
    path('account/', include('user_account.urls')),
    path('api/', include('api.urls')),
]
