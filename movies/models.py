from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# def validate_year(value):
#     current_year = timezone.now().year
#     if value < 1800 or value > current_year:
#         raise ValidationError(f"{value} is an incorrect year. Choose between 1800 and {current_year}")
    

class GenreChoices(models.TextChoices):
    ACTION = 'AC', 'Action'
    DRAMA = 'DR', 'Drama'
    COMEDY = 'CO', 'Comedy'
    HORROR = 'HO', 'Horror'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SF', 'Science Fiction'
    FANTASY = 'FA', 'Fantasy'
    DOCUMENTARY = 'DO', 'Documentary'
    THRILLER = 'TH', 'Thriller'
    ACTION_COMEDY = "ACC", "Action comedy"
    ACTION_HORROR = "ACH", "Action horror"
    HORROR_THRILLER = "HT", "Horror thriller"
    ACTION_THRILLER = "AT", "Action thriller"
    WESTERN = "W", "Western"



class Movie(models.Model):
    Title = models.CharField(max_length=255)  
    Director = models.CharField(max_length=500)
    Release_date = models.DateField()
    # Release_date = models.DateField(validators=[ validate_year])
    Genre = models.CharField(choices=GenreChoices, default=GenreChoices.ACTION, max_length=4)
    Description = models.TextField(max_length=300)
    Poster = models.ImageField(upload_to="movie_poster/", blank=True, null=True)

    def __str__(self):
        return f" Title: {self.Title}, {self.Description}, {self.Genre}, released date {self.Release_date}"
