from typing import no_type_check
from django.db import models
from datetime import datetime
from django.db.models.expressions import F

from requests.api import post


class PersonalMenu(models.Model):
    user_id = models.IntegerField(null=True)
    dish = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.dish


class DishItem(models.Model):
    item = models.CharField(max_length=255, null=True)
    dish = models.ForeignKey(PersonalMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class GroceryCategory(models.Model):
    category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category


class GroceryItem(models.Model):
    item = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(GroceryCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class GroceryListName(models.Model):
    user_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class GroceryList(models.Model):
    name = models.ForeignKey(GroceryListName, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=255, null=True)
    favorite = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True)

    def __str__(self):
        return self.item


class Favorite(models.Model):
    item = models.CharField(max_length=255, null=True)
    user_id = models.IntegerField(null=True)


    def __str__(self):
        return self.item


class UserPost(models.Model):
    user_name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    post = models.TextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class UserComments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, null=True)
    date = models.DateField(auto_now=True, null=True)
    
    
    def __str__(self):
        return self.comment


