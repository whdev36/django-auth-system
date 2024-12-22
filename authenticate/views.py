from django.shortcuts import render
from django.http import HttpResponse

# Home
def home(request):
    return HttpResponse('home')

# Register
def register_user(request):
    return HttpResponse('register')

# Login
def login_user(request):
    return HttpResponse('login')

# Logout
def logout_user(request):
    return HttpResponse('logout')

# Profile
def profile(request):
    return HttpResponse('profile')

# Update profile
def update_profile(request):
    return HttpResponse('update profile')

# Delete profile
def delete_profile(request):
    return HttpResponse('delete profile')