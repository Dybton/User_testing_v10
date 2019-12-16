from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Content
from django.db.models import Avg, Count, Min, Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


@login_required(login_url="homepage")
def home(request):
    # content = Content.objects.annotate(avg=Avg('review__avg_rating')) - Note this is the old one
    content = Content.objects.annotate(avg1=Avg(
        'review__readability_rating'), avg2=Avg('review__actionability_rating'))
    return render(request, 'content/home.html', {'content': content})


def homepage(request):
    return render(request, 'content/homepage.html')


@login_required(login_url="/accounts/signup")
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']:
            content = Content()
            content.title = request.POST['title']
            content.body = request.POST['body']
            content.save()
            return redirect('/content/link/' + str(content.id))
        else:
            return render(request, 'content/add.html', {'error': 'You need to fill in all information'})
    else:
        return render(request, 'content/add.html')


@login_required(login_url="/accounts/signup")
def details(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, 'content/details.html', {'content': content})


@login_required(login_url="/accounts/signup")
def link(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, 'content/link.html', {'content': content})


def readerpage(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    # get the data I need here, store it in variable and pass it as something else
    return render(request, 'content/readerpage.html', {'content': content})


def add_review(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    if request.POST['readability'] and request.POST['readability_rating'] and request.POST['actionability'] and request.POST['actionability_rating'] and request.POST['general_comments']:
        review = Review()
        review.readability = request.POST['readability']
        review.readability_rating = request.POST['readability_rating']
        review.actionability = request.POST['actionability']
        review.actionability_rating = request.POST['actionability_rating']
        review.general_comments = request.POST['general_comments']
        review.avg = (float(review.readability_rating) +
                      float(review.actionability_rating)) / 2
        review.content = content
        review.save()
        return redirect('home')
    else:
        return HttpResponseRedirect(reverse('readerpage', args=(content_id,)))
        # return render (request, 'content/readerpage', {'error': 'You need to fill in all information'})

        # make the quesry and store it in content.reviews.total
