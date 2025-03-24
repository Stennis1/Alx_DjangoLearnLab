from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
]