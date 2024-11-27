from django.db import models
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='author_profiles/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(
        upload_to='book_covers/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.book.title}"

    class Meta:
        unique_together = ('book', 'user')
