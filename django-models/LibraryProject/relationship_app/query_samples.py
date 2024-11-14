from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

if __name__ == "__main__":
    print("Books by Author:", get_books_by_author("Author Name"))
    print("Books in Library:", get_books_in_library("Library Name"))
    print("Librarian for Library:", get_librarian_for_library("Library Name"))
