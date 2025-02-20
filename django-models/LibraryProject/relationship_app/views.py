from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def list_books(request):
    """Function to display list of books"""
    books = Book.objects.all()    
    return render(request, 'relationship_app/list_books.html', {'list_books': books})


class LibraryDetailView(DetailView):
     model = Library
     template_name = 'realtionship_app/library_details.html'
     context_object_name = 'library'