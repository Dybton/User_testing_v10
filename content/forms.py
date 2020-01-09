from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea)
    readability_rating = forms.ChoiceField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    readability = forms.CharField(widget=forms.Textarea)
    actionability_rating = forms.ChoiceField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    actionability = forms.CharField(widget=forms.Textarea)
    general_comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ['name', 'readability_rating', 'readability',
                  'actionability_rating', 'actionability', 'general_comments']
