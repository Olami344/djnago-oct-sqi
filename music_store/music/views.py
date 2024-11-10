from django.shortcuts import render

from .models import Album, Artist

# Create your views here.

def home(request):
    return render (request, "pages/home.html")

def album_listing(request):
    all_albums = Album.objects.order_by("release_date")
    context = {"albums": all_albums}
    return render (request, "music/albums.html", context)

def artist_listing(request):
    all_artists = Artist.objects.order_by("debut_year")
    context = {"albums": all_artists}
    return render (request, "music/artists.html", context)