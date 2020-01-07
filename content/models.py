from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import Avg, Count, Min, Sum


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    reviews_total = models.FloatField(null=True)

    def _str_(self):
        return self.title


class Review(models.Model):
    content = models.ForeignKey(Content, null=True, on_delete=models.CASCADE)
    readability = models.CharField(null=True, max_length=500)
    readability_rating = models.IntegerField(null=True)
    actionability = models.CharField(null=True, max_length=500)
    actionability_rating = models.IntegerField(null=True)
    general_comments = models.CharField(null=True, max_length=500)
    avg_rating = models.FloatField(null=True)

    def _str_(self):
        return self.title


# 1. What is the aggregated avg value of readability rating? - make a function?
# 2. What is the aggretaged avg value of actionability rating?
# 3. What is the aggregated avg value of them both?
# 4. What is the aggregated avg value for all ratings
