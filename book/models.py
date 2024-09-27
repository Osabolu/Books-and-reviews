from django.db import models
# from author.models import Author
# from review.models import Review


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title}, published on {self.book}"


    