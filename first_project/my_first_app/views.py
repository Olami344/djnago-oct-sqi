from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello. This is my first Django view.")

def myself(request):
    return HttpResponse("my name is Solomon")