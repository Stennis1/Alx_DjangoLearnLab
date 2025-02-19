from relationship_app.models import Author, Book, Library, Librarian

# Particular author
# author_name = "J.K. Rowling" 
# author = 
Author.objects.filter(author=author)
Author.objects.get(name=author_name)
# books_by_author = author.books.all()


# List all books in a Library 
# library_name = "Slytherin"
# library = 
Library.objects.get(name=library_name)
# books_in_library = library.books.all()


# Retrieve the librarian for a library
# librarian = 
Librarian.objects.filter(library=library)
Librarian.objects.get(name=library_name)
