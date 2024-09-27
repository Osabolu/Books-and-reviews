from django.shortcuts import render
from .models import Book
from review.models import Review

# Create your views here.

readers_review = {
        "Caleb": "If you love family, loyality, and despise betrayal, The Godfather is your book",
        "Jack": "Dean brown is the man of the year...",
        "Kerry": "Sydney Shelson will make you emotional and keep you at the edge of you seat",
        "Travis": "Mario Puzzo is the real Last Don",
        "shella": "Ben Carlson is an inspiration to black communities around the world", 
    }


context = {
        'reviews': readers_review,
        }
def home(request):
    return render(request, "book/home.html")
def book(request):
    return render(request, "book/book.html")


def review(request):
    return render(request, "book/review.html", context)

def new_book(request):
    all_books = Book.objects.all()
    all_reviews = Review.objects.all()
    context = {
        "all_books": all_books,
        "all_reviews": all_reviews,
    }
   
    return render(request, "artist/new-book.html", context)

def new_review(request):

    all_books = Book.objects.all()
    all_reviews = Review.objects.all()

    context = {
        "all_books": all_books,
        "all_reviews": all_reviews,
    }
    return render(request, "book/new_review.html, context")

