from grocery.models import GroceryListName
from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.contrib.auth.models import User
import ast, json
from rest_framework import serializers, viewsets, permissions
from .serializer import *




class GroceryListView(viewsets.ModelViewSet):
    queryset = GroceryListName.objects.all()
    serializer_class = ListNameSerializer
    permission_class = [permissions.IsAuthenticated]
    
    

@api_view(["GET"])
def getList(request, pk):
    user_lists = GroceryListName.objects.filter(user_id=pk).values('id', 'username', 'name')
    print("hello")
    return Response(list(user_lists))


@api_view(["POST"])
def createList(request):
    print(request.data["listname"])
    
    current_user = request.user  
    listname = request.data["listname"]
    username = User.objects.get(username=current_user)
    exising_name = GroceryListName.objects.filter(username=username, name=listname)
    if not exising_name:
        GroceryListName.objects.create(username=username, user_id=username.id, name=listname)
    user_lists = GroceryListName.objects.filter(user_id=username.id).values('id', 'name')
    
    return Response({"result": list(user_lists)})

    