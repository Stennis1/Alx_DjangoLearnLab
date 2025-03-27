from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreateForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Comment
from django.db.models import Q
from taggit.models import Tag

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
@login_required
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

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm 
    template_form = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.request.POST.get('post_id'))
        form.instance.post = post
        form.instance.author = self.request.author
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.post.id])

class CommentListView(ListView):
    model = Comment 
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

    def get_query_set(self):
        post = get_object_or_404(Post, id=self.request.GET.get('post_id'))
        return Comment.objects.filter(post=post)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment 
    template_name = 'blog/comment_update.html'
    fields = ['content']

    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.post.id])
    
    def test_func(self):
        return self.request.user == self.get_object().author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment 
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.post.id])
    
    def test_func(self):
        return self.request.user == self.get_object().author
    
def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()

    return render(request, 'blog/search_results.html', {'query': query, 'posts': posts})

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['tag'])
        return Post.objects.filter(tags=tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context