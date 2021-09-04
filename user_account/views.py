from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from grocery.models import *


def signup_view(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        # user_signup = authenticate(username=username, password1=password1)
        # login(request, user_signup)
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            user_id = request.session["_auth_user_id"]
            GroceryListName.objects.create(user_id=user_id, name="Favorite")
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                print(request.POST.get('next'))
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'loginA.html')
    return render(request, 'loginA.html')


def logout_view(request):
    logout(request)
    return redirect('/')
