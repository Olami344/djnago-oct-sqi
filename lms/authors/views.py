from django.shortcuts import render

# Create your views here.
def all_authors(request):
    return render (request, "authors/all_authors.html")
