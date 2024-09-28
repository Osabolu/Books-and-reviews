from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .form import ReviewForm, ReviewManualForm
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
    books = Book.objects.all()
    return render(request, "book/book.html", {"books": books})

def book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request,"book/book_view.html", {"book":book})


def review(request):
    return render(request, "book/review.html", context)

def django_form(request):
    return render(request, "book/djangio-form.html")

def new_book(request, book_id):
    all_books = Book.objects.all()
    all_reviews = Review.objects.all()
    context = {
        "all_books": all_books,
        "all_reviews": all_reviews,
    }
    book = get_object_or_404(Book, pk=book_id)
   
    return render(request, "book/new-book.html", context, {"books":book})

def new_review(request):

    all_books = Book.objects.all()
    all_reviews = Review.objects.all()

    context = {
        "all_books": all_books,
        "all_reviews": all_reviews,
    }
    return render(request, "book/new_review.html", context)


def django_form(request):
    form = ReviewManualForm()
    if request.method == "POST":
        form = ReviewManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get("title")
            author = cleaned_data.get("author")
            number_of_pages = cleaned_data.get("number_of_pages")
            published_on = cleaned_data.get("published_on")
            cover_page = cleaned_data.get("cover_page")

            reviewer_name = cleaned_data.get("reviewer")
            book = cleaned_data.get("book")
            rating = cleaned_data.get("rating")
            created_at = cleaned_data.get("created_at")
            picture = cleaned_data.get("picture")
            Review.objects.create(reviewer_name=reviewer_name, book=book, rating=rating, created_at=created_at, picture=picture)
            return redirect("book:book_view")
    
    context = {
        "manual_book_form": form, 
    }
    return render(request, "book/django-form.html", context)





# def django_form(request):
#     form = ReviewForm()
#     if request.method == "POST":
#         print(request.POST)
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("book:new_review")
        
#     context = {
#         "add_book_form": form,
#     }
#     return render(request, "book/django-form.html", context)

