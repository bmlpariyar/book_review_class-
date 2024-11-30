from django.shortcuts import render, redirect, HttpResponse
from user_auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from BookReview.models import Review, Comment
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserProfile
import json
from django.contrib.auth.decorators import login_required




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
            auth_login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {"form": form}) 

def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def user_profile(request):
    req_user = request.user
    review = Review.objects.filter(user=req_user)
    comments = Comment.objects.filter(user=req_user)
    users = User.objects.all()
    context = {"reviews": review,"comments": comments, "users": users}
    return render(request, 'auth/user_profile.html', context)
@login_required
def edit_user_profile(request):
    return render(request, 'auth/edit_user_profile.html')



@csrf_exempt
def admin_update(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_id = body.get('user_id')
            is_admin = body.get('is_admin')

            user_profile = UserProfile.objects.get(user__id=user_id)
            user_profile.is_admin = is_admin
            user_profile.save()

            return JsonResponse({'success': True, 'message': 'Admin status updated successfully.'}, status=200)
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)