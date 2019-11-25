from django.db import models
from django.contrib.auth.models import User
from django import forms


class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # How can I assign the reviews to the content?

    # avg_rating = models.IntegerField(default=0)
    # creator =
    # hunter is set equal to the user, which is a foreign key, as it's in another database, users. Using foreign key us a way to connect multiple models to the database
    # foreign key is saying that we should get the id from the other model, on_delete is just saying that if user is deleted to is product

    def _str_(self):
        return self.title


class Review(models.Model):
    readability = models.CharField(max_length=500)
    readability_rating = models.IntegerField()
    actionability = models.CharField(max_length=500)
    actionability_rating = models.IntegerField()
    general_comments = models.CharField(max_length=500)


# Hvillen værdi får vi fra brugeren og hvilken gør vi ikke?


# title = models.CharField(max_length=3, choices=TITLE_CHOICES)

    #  favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))

    # favorite_colors = forms.MultipleChoiceField(
    #         required=False,
    #         widget=forms.CheckboxSelectMultiple,
    #         choices=FAVORITE_COLORS_CHOICES,

    # readability_rating = forms.MultipleChoiceField(
    #         required=False,
    #         widget=forms.CheckboxSelectMultiple,
    #         choices=CHOICES,
    #         )

    def _str_(self):
        return self.title
