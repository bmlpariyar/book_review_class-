from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages




def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succfully signed up")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # breakpoint()
            auth_login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {"form": form}) 

def logout_user(request):
    logout(request)
    return redirect('index')