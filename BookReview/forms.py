

from .models import Book, Review, Author
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "published_date", "cover_image"]

class ReviewForm(ModelForm):
     class Meta:
        model = Review
        fields = ["rating", "review_text"]


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio", "profile_picture"]
        