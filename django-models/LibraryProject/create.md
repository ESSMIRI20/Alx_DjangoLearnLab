# Create a Book Instance

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected output to confirm successful creation