from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index" ),
    path("book_details/<int:book_id>", book_details, name="book_details" ),
    path("new_book", new_book, name="new_book_from" ),
    path("delete_book/<int:book_id>", delete_book, name="delete_book" ),
    path("edit_book/<int:book_id>", new_book, name="edit_book" ),
    path("add_review/<int:book_id>", add_review, name="add_review" ),
    path("edit_review/<int:review_id>",edit_review, name="edit_review" ),
    path("delete_review/<int:review_id>", delete_review, name="delete_review" ),
    path("add_comment/<int:review_id>", add_comment, name="add_comment" ),
    path("authors/", authors, name="authors" ),
    path("new_author/", create_author, name="new_author" ),
]
