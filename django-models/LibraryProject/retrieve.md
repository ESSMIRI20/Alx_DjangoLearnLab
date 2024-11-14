# Retrieve the Book instance

```python
# Retrieve the Book instance by filtering with the title
book = Book.objects.get(title="1984")
book  # Display the retrieved instance
# Expected output:
# <Book: 1984 by George Orwell (1949)>
# Details:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
