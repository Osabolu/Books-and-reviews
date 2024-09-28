from django import forms
from .models import Book
from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'book', 'rating','picture']


class ReviewManualForm(forms.Form):
    reviewer_name = forms.CharField(max_length=255)
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    rating = forms.IntegerField()
    created_at = forms.DateTimeField()
    picture = forms.ImageField(required=False)