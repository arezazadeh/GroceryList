from grocery.models import *
from rest_framework import serializers


class GroceryListNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryListName
        fields = ["user_id", "name"]
        

class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryList
        fields = ["name", "item"]
        