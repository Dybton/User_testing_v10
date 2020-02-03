from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=10, label='What is your name?')
    interest_rating = forms.ChoiceField(label='How interesting is the piece on a scale of 1-5?',
                                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    interest = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'What is uninteresting? What do you suggest be rewritten to better sustain your interest?', 'cols': 30, 'rows': 4}))
    clarity_rating = forms.ChoiceField(label='Rate how clear you think the piece was on a scale of 1-5',
                                       choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    clarity = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'What’s unclear? Are you left with any unaswered questions?', 'cols': 30, 'rows': 4}))
    brevity_rating = forms.ChoiceField(label='How would you rate the content in terms of brevity on a scale of 1-5',
                                       choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    brevity = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'If you had to delete 20% what would you remove? ', 'cols': 30, 'rows': 4}))
    general_comments = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'General comments? ', 'cols': 30, 'rows': 8}))

    class Meta:
        model = Review
        fields = ['name', 'interest_rating', 'interest',
                  'clarity_rating', 'clarity', 'brevity_rating', 'brevity', 'general_comments']
