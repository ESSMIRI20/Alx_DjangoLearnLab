from django.db import models

# Author model represents an individual author in the system.
# Each author has a name that serves as their identifier.
class Author(models.Model):
    name = models.CharField(max_length=255)  # String field to store the author's name

    def __str__(self):
        return self.name


# Book model represents a book in the system.
# Each book has a title, a publication year, and is associated with an author.
# The relationship between Author and Book is one-to-many, where an author can have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=255)  # String field for the book's title
    publication_year = models.IntegerField()  # Integer field for the book's publication year
    author = models.ForeignKey(
        Author,  # Foreign key links this book to an Author instance
        on_delete=models.CASCADE,  # Ensures books are deleted if the associated author is deleted
        related_name='books'  # Allows reverse access to books via author.books.all()
    )

    def __str__(self):
        return self.title
