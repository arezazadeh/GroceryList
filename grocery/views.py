from django.shortcuts import render, redirect
from .models import *
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login')
def create_list(request):
    print("11111111")
    for k, v in request.session.items():
        print(k, v)
    user_id = request.session['_auth_user_id']
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


@login_required(login_url='/account/login')
def add_to_list(request):
    if request.method == 'POST':
        user_id = request.session['_auth_user_id']
        item_list = request.POST.getlist('item')
        print(request.user)
        for i in item_list:
            user_items = GroceryList.objects.filter(user_id=user_id)
            item_exist = user_items.filter(item=i)
            if not item_exist:
                GroceryList.objects.create(item=i, user_id=user_id)
            else:
                print('Item already in your list')
        return redirect('grocery:create_list')
    return redirect('grocery:create_list')


@login_required(login_url='/account/login')
def view_list(request):
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(user_id=user_id)
    # grocery_list = GroceryList.objects.all()
    return render(request, 'view_list.html', {'list': grocery_list})

@login_required(login_url='/account/login')
def complete(request, item_id): 
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(user_id=user_id)
    grocery_list.filter(id=item_id).update(completed=True)
    
    # grocery_list = GroceryList.objects.all()
    # item = GroceryList.objects.filter(id=item_id)
    # grocery_list.update(completed=True)
    # item.update(completed=True)
    
    return render(request, 'view_list.html', {'list': grocery_list})


@login_required(login_url='/account/login')
def undo_item(request, item_id): 
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(user_id=user_id)
    grocery_list.filter(id=item_id).update(completed=False)
    
    # grocery_list = GroceryList.objects.all()
    # item = GroceryList.objects.filter(id=item_id)
    # item.update(completed=False)
    
    return render(request, 'view_list.html', {'list': grocery_list})


@login_required(login_url='/account/login')
def delete_list(request):
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(user_id=user_id)
    cursor = connection.cursor()
    cursor.execute(f'insert into "grocery_grocerylistarchive" select * from "grocery_grocerylist" where user_id = {user_id} ')
    grocery_list.delete()
    return redirect('grocery:create_list')