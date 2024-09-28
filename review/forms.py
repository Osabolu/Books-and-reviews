# from django import forms
# from .models import Book
# from review.models import Review


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['reviewer_name', 'book', 'ratings','created_in','cover_page']


# class BookManualForm(forms.Form):
#     reviewer_name = forms.CharField(max_length=255)
#     book = forms.ModelChoiceField(queryset=Book.objects.all())
#     rating = forms.IntegerField(1-5)
#     created_in = forms.DateTimeField()
#     cover_page = forms.ImageField(required=False)
    # picture = forms.ImageField(upload_to="review_images/", blank=True, null=True)


# class BookManualForm(forms.Form):
#     reviewer_name = models.CharField(max_length=100)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     rating = models.IntegerField(1-5)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     picture = models.ImageField(upload_to="review_images/", blank=True, null=True)