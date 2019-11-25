from django.db import models
from django.contrib.auth.models import User
from django import forms


class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reviews_total = models.IntegerField(default=0)

    # How can I assign the reviews to the content?

    def _str_(self):
        return self.title


class Review(models.Model):
    # content = models.ForeignKey(Content, on_delete=models.CASCADE)
    readability = models.CharField(max_length=500)
    readability_rating = models.IntegerField()
    actionability = models.CharField(max_length=500)
    actionability_rating = models.IntegerField()
    general_comments = models.CharField(max_length=500)

    def _str_(self):
        return self.title
