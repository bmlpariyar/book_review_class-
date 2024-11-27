from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Review
from .forms import BookForm, ReviewForm
from django.contrib import messages

def index(request):
    books = Book.objects.all()

    context = {"books": books}
    return render(request, "books/book_list.html", context )

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.reviews.all()
    review_ratings = Review.RATING_CHOICES
    context = {"book": book, "reviews": reviews, "review_ratings": review_ratings}
    return render(request, "books/book_details.html", context)



@login_required
def new_book(request, book_id=None):
    book = get_object_or_404(Book, id=book_id) if book_id else None
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            book = form.instance
            return redirect(f"/book_details/{book.id}")
    else:
        form = BookForm(instance=book)
    authors = Author.objects.all()
    return render(request, "books/new_book_form.html", {"form": form, "authors": authors})

@login_required
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)
    



@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        try:
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect(f"/book_details/{book.id}")
        except Exception as e:
            messages.error(request, e)
            return redirect(f"/book_details/{book.id}")
    else:
        form = ReviewForm()
    return redirect(f"/book_details/{book.id}")

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(f"/book_details/{review.book.id}")
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/edit_review.html", {"form": form})
@login_required
def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
        review.delete()
        return redirect(f"/book_details/{review.book.id}")
    except Exception as e:
        messages.error(request, e)
        return redirect(f"/book_details/{review.book.id}")
    
@login_required
def add_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        comment_text = request.POST.get("comment_text")
        comment = review.comments.create(user=request.user, comment_text=comment_text)
        return redirect(f"/book_details/{review.book.id}")
    return redirect(f"/book_details/{review.book.id}")
