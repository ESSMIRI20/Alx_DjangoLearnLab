from django.db import models

# Create your models here.


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100, help_text="Name of the author")

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, help_text="Author of the book")

    def __str__(self):
        return self.title


# Author model represents writers of books
# Book model stores details of books and associates each with an author
