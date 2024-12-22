from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . import models, forms
from django.contrib.auth.decorators import login_required

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
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'u': user})
    else:
        messages.warning(request, 'You need to be logged in to view your profile.')
        return redirect('login')

# Update profile
def update_profile(request):
    if request.method == 'POST':
        form = forms.ProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = forms.ProfileChangeForm(instance=request.user)
    return render(request, 'update-profile.html', {'form': form.as_div()})

# Delete profile
def delete_profile(request):
    return HttpResponse('delete profile')