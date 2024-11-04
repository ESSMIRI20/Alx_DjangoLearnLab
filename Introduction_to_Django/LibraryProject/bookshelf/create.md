# Create a Book Instance

## Command
```python
from yourapp.models import Book  # Adjust 'yourapp' to your app name
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
