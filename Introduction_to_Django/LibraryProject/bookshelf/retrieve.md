```python
from yourapp.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year