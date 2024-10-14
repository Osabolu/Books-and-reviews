from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Movie
from .forms import MovieManualForm
from .forms import MovieForm

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {"movies":movies})

def create(request):
    form = MovieForm()
    if request.method == "POST":
        print(request.POST)
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_list")
    return render(request,"movies/create_movie.html", {"form": form})



def read_detail(request, pk):  
    movie= get_object_or_404(Movie, pk=pk)
    context = {"movie": movie}
    return render(request,'movies/read_detail.html', context)

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(reverse("movies:read_detail", args=[movie_id]))
    context = {"form": form, "movie": movie}
    return render(request, "movies/edit.html", context)
    # movie = get_object_or_404(Movie, pk=movie_id)
    # initial_data = {
    #     "Title": movie.Title,
    #     "Director": movie.Director,
    #     "Genre": movie.Genre,
    #     "Description": movie.Description,
    #     "Release_date": movie.Release_date,
    #     "Poster": movie.Poster,
    # }
    # form = MovieManualForm(initial=initial_data)
    # if request.method == "POST":
    #     form = MovieManualForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         cleaned_data = form.cleaned_data
    #         Title = cleaned_data.get("Title")
    #         Director = cleaned_data.get("Director")
    #         Genre = cleaned_data.get("Genre")
    #         Description = cleaned_data.get("Description")
    #         Release_date = cleaned_data.get("Release_date")  
    #         Poster = cleaned_data.get("Poster")
    #         movie.Title = Title
    #         movie.Director = Director
    #         movie.Genre = Genre
    #         movie.Description = Description
    #         movie.Release_date = Release_date
    #         if Poster:
    #             movie.Poster = Poster
    #         movie.save()
    #         return redirect(reverse("movies:movie_list"))
    # context = {
    #     "form": form,
    #     "movie": movie,
    # }
    # return render(request, "movies/edit.html", context)


# def movie_update(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     initial_data = {
#         "Title": movie.Title,
#         "Director": movie.Director,
#         "Genre": movie.Genre,
#         "Description": movie.Description,
#         "Release_date": movie.Release_date,
#         "Poster": movie.Poster,
#     }
#     form = MovieManualForm(initial=initial_data)
#     if request.method == "POST":
#         form = MovieManualForm(request.POST, request.FILES)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             Title = cleaned_data.get("Title")
#             Director = cleaned_data.get("Director")
#             Genre = cleaned_data.get("Genre")
#             Description = cleaned_data.get("Description")
#             Release_date = cleaned_data.get("Release_date")  
#             Poster = cleaned_data.get("Poster")
#             movie.Title = Title
#             movie.Director = Director
#             movie.Genre = Genre
#             movie.Description = Description
#             movie.Release_date = Release_date
#             if Poster:
#                 movie.Poster = Poster
#             movie.save()
#             return redirect("movies:movie_list")
#     context = {
#         "form": form,
#         "movies": movie,
#     }
#     return render(request, "movies/movie_update.html", context)

def confirm_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    # return redirect("movie:books")
    return render(request,"movies/confirm_delete.html", {"movie":movie})
    # return redirect(reverse("movie:movie", args=[movie_id]))


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        movie.delete()
        return redirect("movies:movie_list")
    return redirect("movies:read_detail")
   



