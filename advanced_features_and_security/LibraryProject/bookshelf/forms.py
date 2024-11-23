# bookshelf/forms.py
from django import forms
from .models import Book  # Assuming you want to create a form for the Book model

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title")
    author = forms.CharField(max_length=100, label="Author Name")
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Published Date")
    description = forms.CharField(widget=forms.Textarea, label="Description")
