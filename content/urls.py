from django.urls import path
from content import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.homepage, name='homepage'),
    path('add/', views.add, name='add'),
    path('<int:content_id>', views.details, name='details'),
    path('link/<int:content_id>', views.link, name='link'),
    path('readerpage/<int:content_id>', views.readerpage, name='readerpage'),
    path('thank_you/<int:content_id>', views.thank_you, name='thank_you'),

]


# path('readerpage/<int:content_id>/add_review',
#      views.add_review, name='add_review'),
