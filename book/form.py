from django import forms
from .models import Book
from review.models import Review
from django.core.validators import MinValueValidator, MaxValueValidator
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


class ReviewManualForm(forms.Form):

    reviewer_name = forms.CharField(max_length=255)
    # rating = forms.IntegerField(validators=[validate_positive])
    rating = forms.IntegerField(validators=[ MinValueValidator(1800),MaxValueValidator(2024)])

    comment = forms.CharField(max_length=500)
    cover_page = forms.ImageField(required=False)
    