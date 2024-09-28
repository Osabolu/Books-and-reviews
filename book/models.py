from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# from author.models import Author
# from review.models import Review


# Create your models here.

def validate_year(value):
    current_year = timezone.now().year
    if value < 1800 or value > current_year:
        raise ValidationError(f"{value} is an incorrect year. Choose between 1800 and {current_year}")
    

class Book(models.Model):
    title = models.CharField(max_length=150)
    author_name = models.CharField(max_length=200, blank=True, null=True)
    publication_date = models.DateField(validators=[validate_year])
    cover_page = models.ImageField(upload_to="book_cover_page/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}, published on {self.publication_date}"


    