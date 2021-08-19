from django.shortcuts import render

from django.http import Http404, HttpResponse
from grocery.models import *
from .serializers import *
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class GroceryListNameView(APIView):
    
    def get(self, request, pk):
        print(pk)
        lists = GroceryListName.objects.filter(pk=pk)
        serializer = GroceryListNameSerializer(lists, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        "retuen a <QueryDict: {'name': ['5'], 'item': ['my stuff']}>"
        data = dict(request.data)
        for k, v in data.items():
            print(list(v)[0])
        "This is how you access it data['item']"
        # grocery_list_name = GroceryListName.objects.filter(pk=pk)
        
        
        post_data = GroceryListSerializer(data=data)
        if post_data.is_valid():
            post_data.save()
            return Response(post_data.data, status=status.HTTP_201_CREATED)
        return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)


