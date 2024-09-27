from django.db import models
from book.models import Book



# Create your models here.

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(1-5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.book}"
