from django import forms
from .models import Book
from review.models import Review
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0 :
        raise ValidationError(f"{value} is not a positive number")
    elif value > 5:
        raise ValidationError(f"{value} 5 is the max number")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating','comment','picture']


class BookManualForm(forms.Form):
    title = forms.CharField(max_length=255)
    author_name =  forms.CharField(max_length=500)   
    publication_date = forms.IntegerField(validators=[validate_positive])
    picture = forms.ImageField(required=False)
 
