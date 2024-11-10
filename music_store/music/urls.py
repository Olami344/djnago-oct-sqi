from django.urls import path
from django.urls import path, include

from . import views

app_name = "music"

urlpatterns =[
    path("home/", views.home, name="home"),
    path("album_listing/", views.album_listing, name="album_listing"),
    path("artist_listing/", views.artist_listing, name="artist_listing"),
]