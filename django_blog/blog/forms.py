from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

class CustomUserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        self.instance.tags.set(*self.cleaned_data['tags'].split())  # Assign tags
        return post

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['content']