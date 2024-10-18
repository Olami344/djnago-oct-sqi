from django.shortcuts import render

# Create your views here.

def favorite(request):
    return render(request, "music/favorite.html")
