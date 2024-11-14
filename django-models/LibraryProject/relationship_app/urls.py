from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL for the class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
