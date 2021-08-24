from datetime import date
from grocery.forms import GroceryListForm
from grocery.api_function import *
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required
import json
from .forms import *


@login_required(login_url='/account/login')
def create_new_list(request):
    user_id = request.session['_auth_user_id']
    current_category = GroceryCategory.objects.all()
    
    if request.method == "POST":
        list_name = request.POST.get('name')
        exising_name = GroceryListName.objects.filter(user_id=user_id, name=list_name)
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

    cursor = connection.cursor()
    user_id = request.session['_auth_user_id']
    
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

        if not new_list:
            list_id = request.POST.get('menu_list_id')

            new_list = GroceryListName.objects.filter(id=list_id)
        for i in item_list:
            user_items = GroceryList.objects.filter(name=new_list[0].id)
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
    grocery_item = grocery_list.filter(id=item_id)
    grocery_item.update(completed=True, date=date.today())
    
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
    grocery_list.delete()
    return redirect('grocery:create_list')


@login_required(login_url='/account/login')
def delete_user_list(request, list_id):
    selected_list = GroceryListName.objects.filter(pk=list_id)
    selected_list.delete()
    return redirect("grocery:user_lists")
    

@login_required(login_url='/account/login')
def add_to_favorite(request, item_id, list_id):
    print("this is add to favorite")
    user_id = request.session["_auth_user_id"]
    grocery_list = GroceryListName.objects.filter(pk=list_id)
    grocery_item = GroceryList.objects.filter(name=grocery_list[0])
    item = grocery_item.filter(pk=item_id)
    add_to_favorite = item.update(favorite=True)
    
    favorite_list = GroceryListName.objects.filter(user_id=user_id, name="Favorite")
    if not favorite_list:
        GroceryListName.objects.create(user_id=user_id, name="Favorite")
        favorite = GroceryListName.objects.filter(user_id=user_id, name="Favorite")
        GroceryList.objects.create(item=item[0].item, name=favorite[0], favorite=True)
    
    else: 
        favorite = GroceryListName.objects.filter(user_id=user_id, name="Favorite")
        GroceryList.objects.create(item=item[0].item, name=favorite[0], favorite=True)
            
    return render(request, 'view_list.html', {'list': grocery_item, 'list_id': list_id})


@login_required(login_url='/account/login')
def remove_from_favorite(request, item_id, list_id): 
    user_id = request.session["_auth_user_id"]
    grocery_list = GroceryListName.objects.filter(pk=list_id)
    grocery_item = GroceryList.objects.filter(name=grocery_list[0])
    item = grocery_item.filter(pk=item_id)
    add_to_favorite = item.update(favorite=False)

    favorite = GroceryListName.objects.filter(user_id=user_id, name="Favorite")
    item = GroceryList.objects.filter(item=item[0].item, name=favorite[0])
    item.delete()
    return render(request, 'view_list.html', {'list': grocery_item, 'list_id': list_id})


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
        
        category = GroceryCategory.objects.filter(category=cat)
        check_for_duplicate = GroceryItem.objects.filter(item=item, category=category[0])
        # check_for_duplicate = GroceryItem.objects.filter(item=item)
        if not check_for_duplicate:
            new_item = GroceryItem.objects.create(item=item, category=category[0])
            messages.success(request, f"{item} added to the Database")
            return redirect("grocery:new_item")
        else:
            messages.error(request, f"{item} already exist in Database")
            return redirect("grocery:new_item")
    return render(request, 'add_item.html', {'cat': current_category})



@login_required(login_url='/account/login')
def create_menu(request):
    if request.method == "POST":
        user_id = request.session['_auth_user_id']
        dish = request.POST.get('dish')
        item_list = request.POST.getlist('item')
        
        new_dish = PersonalMenu.objects.filter(user_id=user_id)
        existing_dish = new_dish.filter(dish=dish)
        
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
        result = food_search(food, cuisine)
        food_list = []
        
        for food in result:
            food_list.append({
                'link': food["_links"]["self"]["href"],
                'image': food["recipe"]["image"],
                'label': food["recipe"]["label"]
            })
        return render(request, 'recipe/recipe_view.html', {'food': food_list})
    return render(request, "recipe/recipe_search.html")


@login_required(login_url='/account/login')
def recipe_detail(request, recipe_link):
    res = get_recipe_detail(recipe_link)
    recipe_id = res["recipe"]["uri"].split("#recipe_")[1]
    res['link'] = res["_links"]["self"]["href"]
    
    return render(request, 'recipe/recipe_detail.html', {'res': res, 'recipe_id': recipe_id})
        

@login_required(login_url='/account/login')
def add_recipe_to_menu(request, recipe_id):
    res = add_recipe_to_personal_menu(recipe_id)

    user_id = request.session["_auth_user_id"]
    
    recipe_name = res["recipe"]["label"]
    menu = PersonalMenu.objects.filter(dish=recipe_name)
    if not menu:
        PersonalMenu.objects.create(user_id=user_id, dish=recipe_name)

    new_menu = PersonalMenu.objects.filter(dish=recipe_name)
    for ing in res["recipe"]["ingredients"]:
        ingredient = ing["text"]
    
        DishItem.objects.create(item=ingredient, dish=new_menu[0])
    return redirect("grocery:menu")
        

@login_required(login_url='/account/login')
def delete_menu(request, menu_id):
    menu = PersonalMenu.objects.filter(pk=menu_id)
    menu.delete()
    return redirect("grocery:menu")


@login_required(login_url='/account/login')
def discussion(request):
    posts = UserPost.objects.all()
    print(posts)

    if request.method == "POST":
        title = request.POST.get('title')
        post = request.POST.get('post')
        user_name = request.user
        # print(title)
        # print()
        # print(post)
        # print(request.user)     
        UserPost.objects.create(user_name=user_name, title=title, post=post)
        posts = UserPost.objects.all()
        return render(request, 'discussion/discussion.html', {'posts': posts})    
    return render(request, 'discussion/discussion.html', {'posts': posts})


@login_required(login_url='/account/login')
def post_detail(request, post_id):
    user_post = UserPost.objects.filter(pk=post_id)
    user_comment = UserComments.objects.filter(post=user_post[0])
    user = request.user
    if request.method == "POST":
        comment = request.POST.get('comment')
        user_post = UserPost.objects.filter(pk=post_id)
        user_name = request.user
        UserComments.objects.create(comment=comment, post=user_post[0], user_name=user_name)
        # return render(request, 'discussion/post.html', {'user_post': user_post, 'user_comment': user_comment, 'post_id': post_id})
        
    return render(request, 'discussion/post.html', {'user_post': user_post[0], 'user_comment': user_comment, 'post_id': post_id})
    
    
@login_required(login_url='/account/login')
def delete_comment(request):
    return redirect("grocery:post")


