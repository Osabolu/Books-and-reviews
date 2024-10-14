from django.db import models
from book.models import Book
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0 :
        raise ValidationError(f"{value} is not a positive number")
    elif value > 5:
        raise ValidationError(f"{value} max number is 5")





# Create your models here.

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[validate_positive])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="review_images/", blank=True, null=True)


    def __str__(self):
        return f"{self.reviewer_name} - {self.book}"
