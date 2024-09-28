
from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path("book/", views.book, name="book"),
    path("review/", views.review, name="review"),
    path("new_book/<int:book_id>/", views.new_book, name="new_book"),
    path("book_view/<int:book_id>", views.book_view, name="book_view"),
    path("home/",views.home, name="home"),
    path("django-form/", views.django_form, name="django_form"),

  


]
