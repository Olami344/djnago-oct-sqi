from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "pages/home.html")

def about(request):
    return render (request, "pages/about.html")

def menu(request):
    return render (request, "pages/menu.html")

def contact(request):
    return render (request, "pages/contact.html")

#  return render (request, "authors/all_authors.html")