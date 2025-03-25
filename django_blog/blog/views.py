from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
# View to handle registration and login
def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successsfully, you can log in now.")
            return redirect('login')
        
    else:
        form = CustomUserCreateForm()
    return render(request, 'blog/register.html', {'form': form})


# Profile required
@login_required 
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')
    else:
        return render(request, 'blog/profile.html', {'user': request.user})


# Logout view 
def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('login')