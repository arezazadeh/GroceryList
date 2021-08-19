from django.db import models
from datetime import datetime


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
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.item


class GroceryListArchive(models.Model):
    user_id = models.IntegerField(null=True)
    item = models.CharField(max_length=255, null=True)
    completed = models.CharField(max_length=255, null=True)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.item
    
