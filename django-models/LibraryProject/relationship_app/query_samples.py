import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

# Import models after setting up Django
from relationship_app.models import Author, Book, Library, Librarian

# Define the functions

# Query all books by a specific author using filter
def get_books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    if authors.exists():
        books = Book.objects.filter(author__in=authors)  # Filter books by the found authors
        return books
    else:
        return f"No author found with name {author_name}"

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# Example Usage (for testing purposes)
if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual data for testing
    print("Books by Author:", get_books_by_author("Author Name"))
    print("Books in Library:", get_books_in_library("Library Name"))
    print("Librarian for Library:", get_librarian_for_library("Library Name"))
