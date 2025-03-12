
Books.objects.filter(author=author)

library.books.all()

# Library.objects.get(librarian__name='John Doe') 
Librarian.objects.get(library=library)