from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from grocery.models import *

from .forms import UserRegisterForm


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
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
