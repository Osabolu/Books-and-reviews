from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .form import ReviewForm
from review.forms import BookManualForm
from .models import Book
from review.models import Review



# Create your views here.

readers_review = { 
        "Caleb": "If you love family, loyality, and despise betrayal, The Godfather is your book",
        "Jack": "Dean brown is the man of the year...",
        "Kerry": "Sydney Sheldon will leave you emotional and keep you at the edge of you seat",
        "Travis": "Mario Puzzo is the real Last Don",
        "sheila": "Ben Carlson is an inspiration to black communities", 
}


context = {
        'reviews': readers_review,
        }

def home(request):
    return render(request, "books/home.html")

def books(request):  
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    context = {
        "book":book,
        "reviews":reviews,
        "form":form
    }
    return render(request,"books/book_detail.html", context)


def review(request, book_id):
    book = get_object_or_404(Book, pk=book_id )
    context = {
        'reviews': readers_review,
        "book":book
        }
    return render(request, "books/review.html", context)


def django_form(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review = Review.objects.filter(book=book)
    form = ReviewForm()
    if request.method == "POST":
        print(request.POST)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("book:book_detail", args=[book_id]))
    context = {
        "book_form": form,
        "review":review,
        "form":form,
        "book": book,
    }
    return render(request, "books/django-form.html", context)

def book_form_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    initial_data = {
        "title": book.title,
        "author_name": book.author_name,
        "publication_date": book.publication_date,
        "cover_page": book.cover_page,
    }
    form = BookManualForm(initial=initial_data)
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get("title")
            author_name = cleaned_data.get("author_name")
            publication_date = cleaned_data.get("publication_date")
            cover_page = cleaned_data.get("cover_page")
            book.title = title
            book.author_name = author_name
            book.publication_date = publication_date
            if cover_page:
                book.cover_page = cover_page
            book.save()
            return redirect("book:books")
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/book-form-update.html", context)




def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()                           
    return redirect("book:books")
        
    
        
        

def confirm_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return redirect("book:books")
    # return render(request,"books/confirm-delete.html", {"book":book})
    return redirect(reverse("book:books", args=[book_id]))
















