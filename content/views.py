from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Content

# Create your views here.


@login_required(login_url="homepage")
def home(request):
    content = Content.objects
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
        return redirect('home')
    else:
        return render(request, 'content/readerpage', {'error': 'You need to fill in all information'})
# def add_review(request, content_id):

# Will try adding a new view function for this functionality - am not strong enough in python to make a proper function
# Create url
# Fix the template
# Add_review får postet en content_id??? hmm.


# is_private = request.POST.get('is_private', False)

# This is before I try to simplify it!
# def add_review(request):
#     if request.method == 'POST':
#         if request.POST['readability']:
#             review = Review()
#             review.readability = request.POST['readability']
#             review.save()
#             return redirect('')
#         else:
#             return render(request, 'content/readerpage.html', {'error': 'You need to fill in all information'})
#     else:
#         return render(request, 'content/readerpage.html')
