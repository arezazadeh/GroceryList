from django.db import models
from django.db.models import fields
from django.http import request
from tastypie.resources import ModelResource
from grocery.models import *


class GroceryListNameResource(ModelResource):
    class Meta:
        queryset = GroceryListName.objects.all()
        resource_name = 'list_name'
        
class GroceryListResource(ModelResource):
    class Meta:
        limit = 99999            
        queryset = GroceryList.objects.all()
        fields = ["name", "completed", "item", "id"]
        resource_name = 'list'
        
        