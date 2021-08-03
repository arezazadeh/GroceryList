from django.shortcuts import render, HttpResponse
from grocery.models import *


def home(request):
    if request.method == "POST":
        cat = request.POST.get('cat')
        item = request.POST.get('item')
        # carb = GroceryCategory.objects.create(category="Cooking")
        # category = GroceryCategory.objects.filter(category=cat)
        # new_item = GroceryItem.objects.create(item=item, category=category[0])

        category = GroceryCategory.objects.filter(category=cat)
        cat_item = GroceryItem.objects.filter(category=category[0])



        return render(request, 'home.html', {'item': cat_item})
    return render(request, 'home.html')