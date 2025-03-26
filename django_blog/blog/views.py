from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreateForm, PostForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
# View to handle registration and login
def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successsfully, you can log in now.")
            return redirect('post-list')
        
    else:
        form = CustomUserCreateForm()
    return render(request, 'blog/register.html', {'form': form})


# Profile required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    else:
        return render(request, 'blog/profile.html', {'user': request.user})


# Logout view 
def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('login')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  #only author can edit
    
class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return super().request.user == post.author