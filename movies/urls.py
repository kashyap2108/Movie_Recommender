
from django.conf.urls import url
from django.contrib import admin

from . import views as movies_views

urlpatterns = [
    url(r'^$',movies_views.home,name='movies_home' ),
    url(r'genre/(?P<genre>[\w\-_]+)/',movies_views.movies_genre_wise,name='movies_genre'),
   	url(r'^autocomplete_city/$',movies_views.autocomplete,name='ac'),
]
