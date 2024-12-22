from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . import models, forms

# Home
def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

# Register
def register_user(request):
    if request.method == 'POST':
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = forms.RegisterUser()
    return render(request, 'register.html', {'form': form.as_div()})

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html', {})

# Logout
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
        return redirect('login')
    return render(request, 'logout.html', {})

# Profile
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'u': user})

# Update profile
def update_profile(request):
    return HttpResponse('update profile')

# Delete profile
def delete_profile(request):
    return HttpResponse('delete profile')