from relationship_app.models import Author, Book, Library, Librarian

# Particular author 
books_by_author = author.books.all()


# List all books in a Library 
books_in_library = library.books.all()


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)