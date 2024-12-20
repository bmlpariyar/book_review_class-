
from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "published_date", "cover_image"]

class ReviewForm(forms.ModelForm):
     class Meta:
        model = Review
        fields = ["rating", "review_text"]
