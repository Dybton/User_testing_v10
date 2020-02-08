from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import Avg, Count, Min, Sum


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    reviews_total = models.FloatField(null=True)
    pub_date = models.DateTimeField(null=True)

    def _str_(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Review(models.Model):
    content = models.ForeignKey(Content, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=500)
    pub_date = models.DateTimeField(null=True)
    interest = models.CharField(null=True, max_length=500)
    interest_rating = models.IntegerField(null=True)
    clarity = models.CharField(null=True, max_length=500)
    clarity_rating = models.IntegerField(null=True)
    brevity = models.CharField(null=True, max_length=500)
    brevity_rating = models.IntegerField(null=True)
    general_comments = models.CharField(null=True, max_length=500)
    avg_rating = models.FloatField(null=True)
    id = models.AutoField(primary_key=True)

    def _str_(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# 1. What is the aggregated avg value of readability rating? - make a function?
# 2. What is the aggretaged avg value of actionability rating?
# 3. What is the aggregated avg value of them both?
# 4. What is the aggregated avg value for all ratings
