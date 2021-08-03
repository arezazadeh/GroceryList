from django.shortcuts import render, redirect
from .models import *
from django.db import connection, transaction



def create_list(request):
    all_item = GroceryItem.objects.all()
    if request.method == "POST":
        cat = request.POST.get('cat')
        item = request.POST.get('item')
        # carb = GroceryCategory.objects.create(category="Cooking")
        # category = GroceryCategory.objects.filter(category=cat)
        # new_item = GroceryItem.objects.create(item=item, category=category[0])

        category = GroceryCategory.objects.filter(category=cat)
        cat_item = GroceryItem.objects.filter(category=category[0])

        return render(request, 'grocery.html', {'item': cat_item})
    return render(request, 'create_list.html')


def add_to_list(request):
    if request.method == 'POST':
        item = request.POST.getlist('item')
        print(item)
        for i in item:
            exists = GroceryList.objects.filter(item=i)
            if not exists:
                GroceryList.objects.create(item=i)
            else:
                print('Item already in your list')
    return redirect('grocery:create_list')


def view_list(request):
    grocery_list = GroceryList.objects.all()
    return render(request, 'view_list.html', {'list': grocery_list})


def complete(request, item_id): 
    grocery_list = GroceryList.objects.all()
    item = GroceryList.objects.filter(id=item_id)
    item.update(completed=True)
    return render(request, 'view_list.html', {'list': grocery_list})


def undo_item(request, item_id): 
    grocery_list = GroceryList.objects.all()
    item = GroceryList.objects.filter(id=item_id)
    item.update(completed=False)
    return render(request, 'view_list.html', {'list': grocery_list})


def delete_list(request):
    cursor = connection.cursor()
    cursor.execute(f'insert into "grocery_grocerylistarchive" select * from "grocery_grocerylist" ')
    GroceryList.objects.all().delete()
    return redirect('grocery:create_list')