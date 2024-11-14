from django.contrib import admin
from .models import Book

# Custom admin class for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filters for publication year and author
    list_filter = ('publication_year', 'author')
    
    # Add a search bar for the title and author fields
    search_fields = ('title', 'author')
