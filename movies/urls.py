from django.urls import path
from . import  views
app_name = "movies"
urlpatterns = [
    path("movie_list/", views.movie_list, name="movie_list"),
    path("read_detail/<int:pk>/", views.read_detail, name="read_detail"),
    path("create/", views.create, name="create"),
    # path("movie_update/<int:movie_id>/", views.movie_update, name="movie_update"),
    path("delete_movie/<int:movie_id>/", views.delete_movie, name="delete_movie"),
    path("edit_movie/<int:movie_id>/", views.edit_movie, name="edit_movie"),
    path("confirm_delete/<int:movie_id>/", views.confirm_delete, name="confirm_delete"),

]

