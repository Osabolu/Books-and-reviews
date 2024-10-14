from django import forms
from .models import Movie
from . forms import Movie
from django.utils import timezone
from django.core.exceptions import ValidationError
# from django.core.validators import MinValueValidator, MaxValueValidator
# from datetime import datetime



# def validate_year(value):
#     current_year = timezone.now().year
#     if value < 1800 or value > current_year:
#          raise ValidationError(f"{value} is an incorrect year. Choose between 1800 and {current_year}")

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['Title', 'Director', 'Release_date','Genre','Description', 'Poster']


class MovieManualForm(forms.Form):
    Title= forms.CharField(max_length=255)
    Director = forms.CharField(max_length=500)        
    Release_date = forms.DateField(required=False, input_formats="%Y-%m-%d")
    # Release_date = forms.IntegerField(validators=[ MinValueValidator(1800),MaxValueValidator(2024)])
    Genre = forms.CharField(max_length=100)
    Description = forms.CharField(max_length=300)
    Poster = forms.ImageField(required=False)

           