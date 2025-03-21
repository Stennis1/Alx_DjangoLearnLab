from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView 
from .models import Book, Library

# Create your views here.

def home(request):
    return redirect("list_books")

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'
    context_object_name = "library"