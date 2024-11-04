
### `delete.md`

```markdown
# Delete the Book Instance

## Command
```python
from yourapp.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify by retrieving all books
Book.objects.all()
