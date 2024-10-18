from django.shortcuts import render
# from authors.models import authors

# Create your views here.
def home(request):
    return render(request, "library/home.html")

def book_list(request):
    return render(request, "library/book_list.html")
