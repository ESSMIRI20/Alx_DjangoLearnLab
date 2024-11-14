# Delete the Book instance

```python
# Delete the Book instance
book.delete()

# Attempt to retrieve all Book instances to confirm deletion
books = Book.objects.all()
books  # Expected output: <QuerySet []>
# Confirming deletion:
# []
