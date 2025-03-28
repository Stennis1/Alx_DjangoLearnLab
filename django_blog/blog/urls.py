from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search_posts, name='search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='tagged-posts'),    
]