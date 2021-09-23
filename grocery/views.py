from datetime import date
from django.http.response import JsonResponse
from grocery.api_function import *
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from notifications.signals import notify
from notifications.models import Notification
import re




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
    return render(request, 'create_new_list.html')



@login_required(login_url='/account/login')
def create_list(request, list_id):

    user_id = request.session['_auth_user_id']
    
    print("````````````````")
    for k, v in request.session.items():
        print(k, v)
    print("````````````````")
    
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
    user_id = request.session['_auth_user_id']
    if request.method == 'POST':
        list_name = request.POST.get('list')
        item_list = request.POST.getlist('item')
        new_list = GroceryListName.objects.filter(id=list_id)
        print(new_list)
        print(item_list)

        if not new_list:
            list_id = request.POST.get('menu_list_id')

            new_list = GroceryListName.objects.filter(id=list_id)
        for i in item_list:
            user_items = GroceryList.objects.filter(name=new_list[0].id)
            item_exist = user_items.filter(item=i)
            if not item_exist:
                if "/" in i:
                    new_item = i.replace("/", ".")
                    GroceryList.objects.create(item=new_item, name=new_list[0])
                else:
                    GroceryList.objects.create(item=i, name=new_list[0])
                
            else:
                print('Item already in your list')
        grocery_list = GroceryList.objects.filter(name=list_id)
        return render(request, 'view_list.html', {'list': grocery_list, 'list_id': list_id})
    return redirect('grocery:create_list', {'list_id': list_id})



@login_required(login_url='/account/login')
def add_custom_item_to_list(request, list_id):
    user_id = request.session['_auth_user_id']
    if request.method == 'POST':
        selected_item = request.POST.get('item').lower()
        list_id = request.POST.get('list_id')

        item = selected_item.replace('/', ".")
        current_list = GroceryListName.objects.filter(id=list_id)
        user_items = GroceryList.objects.filter(name=current_list[0].id)
        fav_list = Favorite.objects.filter(user_id=user_id)
        fav_item = fav_list.filter(item=item)
        item_exist = user_items.filter(item=item)
        if fav_item:
            if not item_exist:
                GroceryList.objects.create(item=item, name=current_list[0], favorite=True)    
            else:
                messages.warning(request, f"{item} already in the list")
        else:
            if not item_exist:
                GroceryList.objects.create(item=item, name=current_list[0], favorite=False)    
            else:
                messages.warning(request, f"{item} already in the list")
        
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


# view Favorite List
@login_required(login_url='/account/login')
def view_fav(request):
    user_id = request.session['_auth_user_id']
    user_list = GroceryListName.objects.filter(user_id=user_id)
    favorite_list = Favorite.objects.filter(user_id=user_id)
    return render(request, 'view_favorite.html', {'fav': favorite_list, 'lists': user_list})



# add Favorited Item to Destination List
@login_required(login_url='/account/login')
def add_to_fav(request):
    user_id = request.session['_auth_user_id']
    user_list = GroceryListName.objects.filter(user_id=user_id)
    favorite_list = Favorite.objects.filter(user_id=user_id)
    if request.method == 'POST':
        list_id = request.POST.get('menu_list_id')
        list_items = request.POST.getlist('item')

        selected_list = GroceryListName.objects.filter(pk=list_id)
        for i in list_items:
            check_for_duplicate = GroceryList.objects.filter(name=selected_list[0], item=i.lower())
            if not check_for_duplicate:
                GroceryList.objects.create(name=selected_list[0], item=i.lower(), favorite=True)
            else:
                messages.warning(request, f"{i} already exists in {selected_list[0].name}")
                return render(request, 'view_favorite.html', {'fav': favorite_list, 'lists': user_list})
    return render(request, 'view_favorite.html', {'fav': favorite_list, 'lists': user_list})



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
    

# Add Item to Favorite from Favorite Form
@login_required(login_url='/account/login')
def add_fav(request):
    if request.method == "POST":
        user_id = request.session['_auth_user_id']
        item = request.POST.get('item').lower()
        check_for_item = Favorite.objects.filter(user_id=user_id, item=item)
        if not check_for_item:
            Favorite.objects.create(user_id=user_id, item=item)
        user_list = GroceryListName.objects.filter(user_id=user_id)
        favorite_list = Favorite.objects.filter(user_id=user_id)
        return render(request, 'view_favorite.html', {'fav': favorite_list, 'lists': user_list})
 

# Delete Item from Favorite In Favorite List
@login_required(login_url='/account/login')
def del_fav(request, item_id):
    user_id = request.session['_auth_user_id']
    check_for_item = Favorite.objects.filter(user_id=user_id)
    item = check_for_item.filter(pk=item_id)
    item.delete()
    
    
    user_list = GroceryListName.objects.filter(user_id=user_id)
    favorite_list = Favorite.objects.filter(user_id=user_id)
    return render(request, 'view_favorite.html', {'fav': favorite_list, 'lists': user_list})
 



# Favorite Items
@login_required(login_url='/account/login')
def favorite_item(request, item_id, item_name, list_id):
    user_id = request.session["_auth_user_id"]
    grocery_list = GroceryListName.objects.filter(pk=list_id)
    grocery_item = GroceryList.objects.filter(name=grocery_list[0])
    
    user_fav_list = Favorite.objects.filter(user_id=user_id)
    existing_item_in_fav = user_fav_list.filter(item=item_name.lower())
    if not existing_item_in_fav:
        add_item_to_fav = Favorite.objects.create(item=item_name.lower(), user_id=user_id)
    else:
        messages.warning(request, "Item Already in Favorite")
        return render(request, 'view_list.html', {'list': grocery_item, 'list_id': list_id}) 
        
    grocery_item.filter(item=item_name).update(favorite=True)
    return render(request, 'view_list.html', {'list': grocery_item, 'list_id': list_id})
# End of Add item to Favorite


# Remove Favorited Item  
@login_required(login_url='/account/login')
def remove_fav_item(request, item_id, item_name, list_id): 
    grocery_list = GroceryListName.objects.filter(pk=list_id)
    grocery_item = GroceryList.objects.filter(name=grocery_list[0])
    item = grocery_item.filter(pk=item_id)
    item.update(favorite=False)
    user_id = request.session["_auth_user_id"]
    favorite_list = Favorite.objects.filter(user_id=user_id)
    fav_item = favorite_list.filter(item=item_name)
    fav_item.delete()
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
        instruction = request.POST.get('instruction')
        
        new_dish = PersonalMenu.objects.filter(user_id=user_id)
        existing_dish = new_dish.filter(dish=dish)
        
        if not existing_dish:
            create_new_dish = PersonalMenu.objects.create(user_id=user_id, dish=dish, instruction=instruction)
            new_dish = PersonalMenu.objects.filter(dish=create_new_dish)

            for item in item_list:
                DishItem.objects.create(item=item, dish=new_dish[0])
            messages.success(request, f"{dish} was added successfully")
            return redirect("grocery:c-menu")
        
        # else statement if the dish already exists         
    return render(request, "add_dish.html")

@login_required(login_url='/account/login')
def update_menu(request, menu_id):
    context = {}
    
    menu_obj = get_object_or_404(PersonalMenu, id=menu_id)
    form1 = menu_obj.dish_items.filter(dish=menu_id)
    
    form = MenuForm(request.POST or None, instance=menu_obj)
    
    if form.is_valid():
        form.save()
        return redirect(f"/grocery/menu_detail/{menu_id}/")
    context["form"] = form
    context["form1"] = form1
    return render(request, 'menu_update_form.html', {'form': form, 'form1': form1, 'menu_id': menu_id})
    
@login_required(login_url='/account/login')
def item_update(request, item_id, menu_id):
    if request.method == 'POST': 
        updated_item = request.POST.get('item')
        print(updated_item)
        menu_id = PersonalMenu.objects.get(id=menu_id)
        item = DishItem.objects.get(id=item_id, dish=menu_id.id)
        item.item = updated_item
        item.save()
        
        return HttpResponse(updated_item)

    return HttpResponse("hello")
    
@login_required(login_url='/account/login')
def add_item_existing_menu(request, menu_id):
    if request.method == "POST":
        item = request.POST.get('item')
        dish = PersonalMenu.objects.get(pk=menu_id)
        DishItem.objects.create(dish=dish, item=item)
        return redirect(f'/grocery/menu/update/{menu_id}/')

@login_required(login_url='/account/login')
def delete_item_from_existing_menu(request, menu_id, item_id):
    item = DishItem.objects.get(pk=item_id, dish=menu_id)
    item.delete()
    
    return redirect(f'/grocery/menu/update/{menu_id}/')
    

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
        mealType = request.POST.get('meal_type')
        result = food_search(food, cuisine, mealType)
        if result is None:
            messages.error(request, "Please modify your search")
            return render(request, "recipe/recipe_search.html")
        else:
            next_page = result[1]
            food_list = []
            for food in result[0]:
                food_list.append({
                    'link': food["_links"]["self"]["href"],
                    'image': food["recipe"]["image"],
                    'label': food["recipe"]["label"]
                })
            return render(request, 'recipe/recipe_view.html', {'food': food_list, 'next': next_page})
    return render(request, "recipe/recipe_search.html")


# api returns around 10000 recipes, where it only shows 20 at a time, where the next page url is embeded in the api return
def recipe_next_page(request, recipe_link):
    result = recipe_next(recipe_link)
    next_page = result[1]
    food_list = []
    for food in result[0]:
        food_list.append({
            'link': food["_links"]["self"]["href"],
            'image': food["recipe"]["image"],
            'label': food["recipe"]["label"]
        })
    return render(request, 'recipe/recipe_view.html', {'food': food_list, 'next': next_page})
    


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
    instruction = res["recipe"]["url"]
    menu = PersonalMenu.objects.filter(dish=recipe_name)
    if not menu:
        PersonalMenu.objects.create(user_id=user_id, dish=recipe_name, instruction=instruction)

    new_menu = PersonalMenu.objects.filter(dish=recipe_name)
    for ing in res["recipe"]["ingredients"]:
        ingredient = ing["text"]
    
        DishItem.objects.create(item=ingredient, dish=new_menu[0])
    return redirect("grocery:menu")
        

@login_required(login_url='/account/login')
def share_recipe(request, recipe_id):
    res = add_recipe_to_personal_menu(recipe_id)
    user_id = request.session["_auth_user_id"]
    recipe_name = res["recipe"]["label"]
    url = res["recipe"]["url"]
    recipe_post = recipe_name + "--" + url
    user_post = UserPost.objects.create(
        user_name=request.user,
        title=recipe_name,
        post=recipe_post
    )
    print(user_post.id)
    return redirect("grocery:discussion")
    # return post_update(request, post_id=user_post.id)
    


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


# class base for discussion home page 

class PostListView(ListView):
    model = UserPost
    template_name = 'discussion/discussion_home.html'
    context_object_name = 'posts'
    ordering = ["-date"]

class PostDetailView(DetailView):
    model = UserPost
    template_name = 'discussion/post_detail.html'

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = UserPost
    fields = ["title", "post"]
    template_name = "discussion/post_form.html"
    success_url = "/grocery/discussion/"
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        post = form.instance.post
        url_pattern = re.compile("(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
        # url = re.findall(url_pattern, post)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserPost
    fields = ["title", "post"]
    template_name = "discussion/post_form.html"
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_name:
            return True
        else:
            return False


@login_required(login_url='/account/login')
def post_update(request, post_id):
    context = {}
    print(post_id)
    obj = get_object_or_404(UserPost, id=post_id)
    print(obj)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(f"/grocery/post_detail/{post_id}/")
    context["form"] = form
    return render(request, 'discussion/user_post_form.html', {'form': form})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserPost
    template_name = 'discussion/post_delete_confirm.html'
    success_url = '/grocery/discussion/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_name:
            return True
        else:
            return False

class CommentCreateView(LoginRequiredMixin ,CreateView):
    model = UserComments
    fields = ["comment"]
    template_name = "discussion/post_detail.html"
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


@login_required(login_url='/account/login')
def post_detail(request, post_id):
    user_post = UserPost.objects.filter(pk=post_id)
    user_comment = UserComments.objects.filter(post=user_post[0])
    
    return render(request, 'discussion/post_detail.html', {'object': user_post, 'user_comment': user_comment, 'post_id':post_id})
    


@login_required(login_url='/account/login')
def comment_add(request, post_id):
    user_post = UserPost.objects.filter(pk=post_id)
    
    user_name = user_post[0].user_name
    user_model = User.objects.get(username=user_name)
    print(user_model)
    user_comment = UserComments.objects.filter(post=user_post[0])
    if request.method == "POST":
        comment = request.POST.get('comment')
        post = request.POST.get('post_id')
        
        # print(b[0])
        # for n in b:
        #     for g in n[1]:
        #         print(g.actor)
        #         print(g.description)
        #         print(g.id)
                    
        # print()
        
        # print()
        # a = Notification.objects.all()
        # for i in a:
        #     print(i.id, i.description)

        user_post = UserPost.objects.filter(pk=post)
        UserComments.objects.create(comment=comment, post=user_post[0], user_name=request.user)
        return render(request, 'discussion/post_detail.html', {'object': user_post, 'user_comment': user_comment, "post_id": post_id})
        
    return render(request, 'discussion/post_detail.html', {'object': user_post, 'user_comment': user_comment, "post_id": post_id})


@login_required(login_url='/account/login')
def comment_update(request, comment_id, post_id):
    context = {}
    print(post_id)
    obj = get_object_or_404(UserComments, id=comment_id)
    print(obj)
    form = CommentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(f"/grocery/post_detail/{post_id}/")
    context["form"] = form
    return render(request, 'discussion/usercomments_form.html', {'form': form})
    
    
# Like or Dislike a Post 

class UpdatePostVote(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        post_id = self.kwargs.get('post_id', None)

        opinion = self.kwargs.get('opinion', None) # like or dislike button clicked

        user_post = get_object_or_404(UserPost, id=post_id)

        if opinion.lower() == 'like':
            print("like")
            liked_already = user_post.likes.filter(user_name=request.user)
            dis_liked_already = user_post.dis_likes.filter(user_name=request.user)
            
            if not liked_already:
                user_post.likes.create(user_name=request.user)
                if dis_liked_already:
                    dis_liked_already.delete()
            else:
                liked_already.delete()
                return redirect(f"/grocery/post_detail/{post_id}/")
            
        if opinion.lower() == 'dis_like':
            print("dis_like")
            liked_already = user_post.likes.filter(user_name=request.user).delete()
            dis_liked_already = user_post.dis_likes.filter(user_name=request.user)
            if not dis_liked_already:
                user_post.dis_likes.create(user_name=request.user)
            else:
                dis_liked_already.delete()
                return redirect(f"/grocery/post_detail/{post_id}/")
        print(user_post.get_total_dis_likes())

        return redirect(f"/grocery/post_detail/{post_id}/")



class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserComments
    fields = ["comment"]
    template_name = "discussion/usercomments_form.html"
    success_url = '/grocery/discussion/'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.user_name:
            return True
        else:
            return False


    
@login_required(login_url='/account/login')
def delete_comment(request, comment_id, post_id):
    comment = UserComments.objects.filter(id=comment_id)
    if comment:
        comment.delete()
        return redirect(f"/grocery/post_detail/{post_id}/")
    return redirect('/')






def api_get(request):
    if request.method == "GET":
        user_id = 2
        menu = PersonalMenu.objects.filter(user_id=user_id).values("dish")
        return JsonResponse({"result": list(menu)})

