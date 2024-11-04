from yourapp.models import Book  # Replace 'yourapp' with the actual app name
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
<Book: Book object (1)>

book = Book.objects.get(title="1984")
(book.title, book.author, book.publication_year)
('1984', 'George Orwell', 1949)

book.title = "Nineteen Eighty-Four"
book.save()
book.title
'Nineteen Eighty-Four'

book.delete()
# Verify by retrieving all books
Book.objects.all()
(1, {'yourapp.Book': 1})

<QuerySet []>