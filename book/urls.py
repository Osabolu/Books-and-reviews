
from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path("books/", views.books, name="books"),
    path("review/<int:book_id>/", views.review, name="review"),
    # path("new_book/", views.new_book, name="new_book"),
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("home/",views.home, name="home"),
    path("django-form/<int:book_id>/", views.django_form, name="django_form"), 
    path("book-form-update/<int:book_id>/", views.book_form_update, name="book_form_update"),
    path("confirm-delete/<int:book_id>/", views.confirm_delete, name="confirm_delete"),
    path("delete/<int:book_id>/", views.delete_book, name="delete_book"),

]
