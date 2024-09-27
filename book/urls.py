
from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path("book/", views.book, name="book"),
    path("review/", views.review, name="review"),
    path("new_book/", views.new_book, name="new_book"),
    path("new_review/", views.review, name="new_review"),
    path("home/",views.home, name="home"),

]
