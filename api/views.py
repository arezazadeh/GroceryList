from grocery.models import GroceryList
from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.contrib.auth.models import User
import ast, json
from rest_framework import serializers, viewsets, permissions
from .serializer import *




class GroceryListView(viewsets.ModelViewSet):
    queryset = GroceryList.objects.all()
    serializer_class = ListNameSerializer
    permission_class = [permissions.IsAuthenticated]
    
    

@api_view(["GET"])
def getList(request, pk):
    user_lists = GroceryList.objects.filter(user_id=pk).values('id', 'username', 'name')
    return Response(list(user_lists))


@api_view(["POST"])
def createList(request):
    print(request.data["listname"])
    
    current_user = request.user  
    listname = request.data["listname"]
    username = User.objects.get(username=current_user)
    exising_name = GroceryList.objects.filter(username=username, name=listname)
    if not exising_name:
        GroceryList.objects.create(username=username, user_id=username.id, name=listname)
    user_lists = GroceryList.objects.filter(user_id=username.id).values('id', 'name')
    
    return Response({"result": list(user_lists)})


@api_view(["GET"])
def view_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return Response(list(users))
    