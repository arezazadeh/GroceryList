from grocery.models import *
from django.contrib.auth.models import User
from rest_framework import serializers



class ListNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryListName
        fields = "__all__"
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

