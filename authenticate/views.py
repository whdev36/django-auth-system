from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . import forms
from django.db.models import Q

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
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            messages.info(request, 'You have been logged out successfully.')
            return redirect('login')
        return render(request, 'logout.html', {})
    else:
        messages.warning(request, 'You are not logged in.')
        return redirect('login')

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
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ProfileChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully.')
                return redirect('profile')
        else:
            form = forms.ProfileChangeForm(instance=request.user)
        return render(request, 'update-profile.html', {'form': form.as_div()})
    else:
        messages.warning(request, 'You need to be logged in to update your profile.')
        return redirect('home')

# Delete profile
def delete_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(User, pk=request.user.pk)
            user.delete()
            messages.success(request, 'Your profile has been deleted successfully.')
            return redirect('home')
        return render(request, 'delete.html', {})
    else:
        messages.warning(request, 'You need to be logged in to delete your profile.')
        return redirect('login')

# Search user
def search(request):
    q = request.GET.get('q', '')
    users = User.objects.none()
    if q and q != '':
        users = User.objects.filter(Q(username__icontains=q) | Q(email__icontains=q) |
                                    Q(first_name__icontains=q) | Q(last_name__icontains=q))
    return render(request, 'search.html', {'users': users})

def user(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user.html', {'u': user})