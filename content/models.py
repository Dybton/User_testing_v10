from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import Avg, Count, Min, Sum


class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reviews_total = models.FloatField(null=True)

    def _str_(self):
        return self.title


class Review(models.Model):
    content = models.ForeignKey(Content, null=True, on_delete=models.CASCADE)
    readability = models.CharField(max_length=500)
    readability_rating = models.IntegerField()
    actionability = models.CharField(max_length=500)
    actionability_rating = models.IntegerField()
    general_comments = models.CharField(max_length=500)
    avg_rating = models.IntegerField(null=True)

    # def avg():
    #     return (actionability_rating + readability_rating) / 2

    # def total_avg_rating (self):
    #     return


# Review.objects.values(
#     'content_id',
#     'content__title',
#     'readability_rating',
#     'actionability_rating'
# ).aggregate(
#     id=F('username_id'),
#     title=F('content__title'),
#     avg_read_rating=Avg('readability_rating'),
#     avg_act_rating=Avg('actionability_rating')
# )

    def _str_(self):
        return self.title

    # def avg_rating(self):
    #     return self.

# 1. What is the aggregated avg value of readability rating? - make a function?
# 2. What is the aggretaged avg value of actionability rating?
# 3. What is the aggregated avg value of them both?
# 4. What is the aggregated avg value for all ratings
