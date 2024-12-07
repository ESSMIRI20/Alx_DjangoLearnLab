from rest_framework import serializers
from .models import Author, Book

# Serializer for the Author model.
# This serializer handles the conversion of Author model instances to JSON format and vice versa.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested relationship: Lists all books by this author
    books = serializers.StringRelatedField(many=True, read_only=True)  # Uses the __str__() of Book for display

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Include author's ID, name, and their related books


# Serializer for the Book model.
# This serializer converts Book model instances to JSON format and allows for creation/update.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Includes all relevant fields of the Book model
