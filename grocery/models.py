from django.db import models
from datetime import datetime

class GroceryCategory(models.Model):
    category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category


class GroceryItem(models.Model):
    item = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(GroceryCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class GroceryList(models.Model):
    user_id = models.IntegerField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.item


class GroceryListArchive(models.Model):
    user_id = models.IntegerField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    completed = models.CharField(max_length=255, null=True)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.item