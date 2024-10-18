from django.urls import path

from . import views



urlpatterns = [
    path("home/", views.home, name="home"),
    path("book_list/", views.book_list, name="books"),
]