from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# Create your views here.
class CustomUserCreationForm(UserCreationForm):
    forms = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

# User registration view 
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successsfully, you can log in now.")
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# Profile required
@login_required 
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})