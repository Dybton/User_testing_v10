from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Content
from django.db.models import Avg, Count, Min, Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.utils import timezone


@login_required(login_url="homepage")
def home(request):
    content = Content.objects.annotate(
        avg=Avg('review__avg_rating')).filter(user=request.user)
    # Also send pub_dateo of the review

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
            content.user = request.user
            content.save()
            return redirect('/content/link/' + str(content.id))
        else:
            return render(request, 'content/add.html', {'error': 'You need to fill in all information'})
    else:
        return render(request, 'content/add.html')


@login_required(login_url="/accounts/signup")
def details(request, content_id):
    content = get_object_or_404(
        Content.objects.annotate(
            avg_rr=Avg('review__readability_rating'),
            avg_ar=Avg('review__actionability_rating'),
            avg=Avg('review__avg_rating')
        ),
        pk=content_id)
    return render(request, 'content/details.html', {'content': content, 'reviews': Review.objects.filter(content_id=content_id)})


@login_required(login_url="/accounts/signup")
def link(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, 'content/link.html', {'content': content})


def readerpage(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.content = content
        readability_rating = form.cleaned_data['readability_rating']
        readability = form.cleaned_data['readability']
        actionability_rating = form.cleaned_data['actionability_rating']
        actionability = form.cleaned_data['actionability']
        general_comments = form.cleaned_data['general_comments']
        review.avg_rating = (float(readability_rating) +
                             float(actionability_rating)) / 2
        review.pub_date = timezone.datetime.now()
        review.save()
        return redirect('home')
    args = {'content': content, 'form': form}
    return render(request, 'content/readerpage.html', args)

# How can I calculate the avg_rating?

# def add_review(request, content_id):
#     content = get_object_or_404(Content, pk=content_id)
#     if request.POST['readability'] and request.POST['readability_rating'] and request.POST['actionability'] and request.POST['actionability_rating'] and request.POST['general_comments']:
#         review = Review()
#         review.readability = request.POST['readability']
#         review.readability_rating = request.POST['readability_rating']
#         review.actionability = request.POST['actionability']
#         review.actionability_rating = request.POST['actionability_rating']
#         review.general_comments = request.POST['general_comments']
#         review.avg_rating = (float(review.readability_rating) +
#                              float(review.actionability_rating)) / 2
#         review.content = content
#         review.save()
#         return redirect('home')
#     else:
#         return HttpResponseRedirect(reverse('readerpage', args=(content_id,)))
