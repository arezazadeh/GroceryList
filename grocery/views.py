from grocery.api_function import food_search, get_recipe_detail
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required



@login_required(login_url='/account/login')
def create_new_list(request):
    user_id = request.session['_auth_user_id']
    current_category = GroceryCategory.objects.all()
    
    if request.method == "POST":
        list_name = request.POST.get('name')
        exising_name = GroceryListName.objects.filter(user_id=user_id, name=list_name)
        print(exising_name)
        if not exising_name:
            GroceryListName.objects.create(user_id=user_id, name=list_name)
        else:
            print("list is there")
            
        new_list = GroceryListName.objects.filter(user_id=user_id, name=list_name)
        user_lists = GroceryListName.objects.filter(user_id=user_id)
        return render(request, 'user_lists.html', {'user_lists': user_lists})    
        # return render(request, 'create_list.html', {'cat': current_category, 'new': False, 'new_list': new_list})
    return render(request, 'create_new_list.html')



@login_required(login_url='/account/login')
def create_list(request, list_id):
    print()
    print(list_id)
    print()
    cursor = connection.cursor()
    user_id = request.session['_auth_user_id']

    # a = cursor.execute(f'insert into "grocery_grocerylistarchive" select * from "grocery_grocerylist" where user_id={user_id}')
    # for i in a:
    #     print(i)
    
    
    print("11111111")
    for k, v in request.session.items():
        print(k, v)
    print("11111111")
    
    current_category = GroceryCategory.objects.all()
    if request.method == "POST":
        cat = request.POST.get('cat')
        list_name = request.POST.get('list_name')
        category = GroceryCategory.objects.filter(category=cat)
        cat_item = GroceryItem.objects.filter(category=category[0])

        return render(request, 'create_list.html', {'item': cat_item, 'cat': current_category, 'list_id': list_id, 'new': True, 'this': cat, 'new_list':list_name})
    return render(request, 'create_list.html', {'cat': current_category, 'new': False, 'list_id': list_id })


@login_required(login_url='/account/login')
def add_to_list(request, list_id):
    print(f"--------- {list_id} -------------")
    user_id = request.session['_auth_user_id']
    if request.method == 'POST':
        list_name = request.POST.get('list')
        item_list = request.POST.getlist('item')
        
        new_list = GroceryListName.objects.filter(id=list_id)
        print("````````````````````")
        print(new_list)
        if not new_list:
            list_id = request.POST.get('menu_list_id')
            print(list_id)
            new_list = GroceryListName.objects.filter(id=list_id)
        print(new_list)
        for i in item_list:
            user_items = GroceryList.objects.filter(name=new_list[0].id)
            print(f"$$$$$$$$$$$$ {user_items}")
            item_exist = user_items.filter(item=i)
            if not item_exist:
                GroceryList.objects.create(item=i, name=new_list[0])
                
            else:
                print('Item already in your list')
        grocery_list = GroceryList.objects.filter(name=list_id)
        return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})
    return redirect('grocery:create_list', {'list_id': list_id})


@login_required(login_url='/account/login')
def view_list(request, list_id):
    grocery_list = GroceryList.objects.filter(name=list_id)
    return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})


@login_required(login_url='/account/login')
def view_lists(request):
    user_id = request.session['_auth_user_id']
    user_lists = GroceryListName.objects.filter(user_id=user_id)
    return render(request, 'user_lists.html', {'user_lists': user_lists})



@login_required(login_url='/account/login')
def complete(request, item_id, list_id): 
    grocery_list = GroceryList.objects.filter(name=list_id)
    grocery_list.filter(id=item_id).update(completed=True)
    return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})
    

@login_required(login_url='/account/login')
def delete_item(request, item_id, list_id): 
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(name=list_id)
    grocery_list.filter(id=item_id).delete()
    return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})


@login_required(login_url='/account/login')
def undo_item(request, item_id, list_id): 
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(name=list_id)
    grocery_list.filter(id=item_id).update(completed=False)
    return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})


@login_required(login_url='/account/login')
def delete_list(request):
    user_id = request.session['_auth_user_id']
    grocery_list = GroceryList.objects.filter(user_id=user_id)
    cursor = connection.cursor()
    cursor.execute(f'insert into "grocery_grocerylistarchive" select * from "grocery_grocerylist" where user_id = {user_id} ')
    grocery_list.delete()
    return redirect('grocery:create_list')


@login_required(login_url='/account/login')
def new_cat(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
        if not cat:
            messages.error(request, f"Please enter a valid Category")
            return redirect("grocery:new_cat")
        existing_category = GroceryCategory.objects.filter(category=cat)
        if not existing_category:
            GroceryCategory.objects.create(category=cat)
            messages.success(request, f"Category {cat} was successfully added")
            return redirect("grocery:new_cat")
        else:
            messages.error(request, f"Category {cat} already exist in Database")
            return redirect("grocery:new_cat")

    return render(request, 'add_to_cat.html')


@login_required(login_url='/account/login')
def new_item(request):
    current_category = GroceryCategory.objects.all()

    if request.method == "POST":
        cat = request.POST.get('cat')
        item = request.POST.get('item')
        print(cat, item)
        
        category = GroceryCategory.objects.filter(category=cat)
        check_for_duplicate = GroceryItem.objects.filter(item=item, category=category[0])
        # check_for_duplicate = GroceryItem.objects.filter(item=item)
        if not check_for_duplicate:
            new_item = GroceryItem.objects.create(item=item, category=category[0])
            print(new_item)
            messages.success(request, f"{item} added to the Database")
            return redirect("grocery:new_item")
        else:
            messages.error(request, f"{item} already exist in Database")
            return redirect("grocery:new_item")
    return render(request, 'add_item.html', {'cat': current_category})


@login_required(login_url='/account/login')
def view_archived(request):
    user_id = request.session['_auth_user_id']
    archived_list = GroceryListArchive.objects.filter(user_id=user_id)
    return render(request, 'archived.html', {'item_list': archived_list})


@login_required(login_url='/account/login')
def create_menu(request):
    if request.method == "POST":
        user_id = request.session['_auth_user_id']
        dish = request.POST.get('dish')
        item_list = request.POST.getlist('item')
        
        new_dish = PersonalMenu.objects.filter(user_id=user_id)
        existing_dish = new_dish.filter(dish=dish)
        print(existing_dish)
        
        if not existing_dish:
            create_new_dish = PersonalMenu.objects.create(user_id=user_id, dish=dish)
            new_dish = PersonalMenu.objects.filter(dish=create_new_dish)

            for item in item_list:
                DishItem.objects.create(item=item, dish=new_dish[0])
            messages.success(request, f"{dish} was added successfully")
            return redirect("grocery:c-menu")
        
        # else statement if the dish already exists 
        
    return render(request, "add_dish.html")


@login_required(login_url='/account/login')
def view_menu(request):
    user_id = request.session["_auth_user_id"]
    dish = PersonalMenu.objects.filter(user_id=user_id)
    return render(request, 'view_menu.html', {'dish': dish})


@login_required(login_url='/account/login')
def view_menu_detail(request, dish_id):
    user_id = request.session["_auth_user_id"]
    dish = PersonalMenu.objects.filter(id=dish_id)
    dish_item = DishItem.objects.filter(dish=dish[0])
    user_list = GroceryListName.objects.filter(user_id=user_id)
    
    return render(request, 'menu_detail.html', {'dish': dish, 'dish_detail': dish_item, 'lists': user_list})


@login_required(login_url='/account/login')
def recipe_search(request):
    if request.method == "POST":
        food = request.POST.get('food')
        cuisine = request.POST.get('cuisine')
        res = food_search(food, cuisine)
        
        
        for food in res:
            recipe = food["recipe"]
            image = recipe["image"]
            ing = recipe["ingredientLines"]
            if "cuisineType" in recipe:
                cuisineType = recipe["cuisineType"]
            else:
                cuisineType = "Not Specified"
            # print(cuisineType, recipe["label"], recipe["url"], image)
            recipe_id = recipe["uri"].split("#")[1]
        return render(request, 'recipe/recipe_view.html', {'food': res, "recipe_id": recipe_id})
    return render(request, "recipe/recipe_search.html")


@login_required(login_url='/account/login')
def recipe_detail(request, recipe_id):
    res = get_recipe_detail(recipe_id)
    print(res["recipe"]["url"])
    # print(json.dumps(res, indent=4))
    return render(request, 'recipe/recipe_detail.html', {'res': res, 'recipe_id': recipe_id})
        

@login_required(login_url='/account/login')
def add_recipe_to_menu(request, recipe_id):
    res = get_recipe_detail(recipe_id)
    user_id = request.session["_auth_user_id"]
    recipe_name = res["recipe"]["label"]
    menu = PersonalMenu.objects.filter(dish=recipe_name)
    if not menu:
        PersonalMenu.objects.create(user_id=user_id, dish=recipe_name)

    new_menu = PersonalMenu.objects.filter(dish=recipe_name)
    for ing in res["recipe"]["ingredients"]:
        ingredient = ing["text"]
    
        DishItem.objects.create(item=ingredient, dish=new_menu[0])
    return render(request, 'recipe/recipe_search.html')
        

