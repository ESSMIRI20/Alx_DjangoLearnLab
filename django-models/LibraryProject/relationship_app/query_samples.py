import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Define the functions

# Query all books by a specific author using get and filter
def get_books_by_author(author_name):
    try:
        # Retrieve the author instance
        author = Author.objects.get(name=author_name)
        # Filter books by the retrieved author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# Retrieve the librarian for a library using Librarian.objects.get
def get_librarian_for_library(library_name):
    try:
        # Retrieve the library instance first
        library = Library.objects.get(name=library_name)
        # Now get the librarian directly based on the library
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library {library_name}"

# Example Usage (for testing purposes)
if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual data for testing
    print("Books by Author:", get_books_by_author("Author Name"))
    print("Books in Library:", get_books_in_library("Library Name"))
    print("Librarian for Library:", get_librarian_for_library("Library Name"))
