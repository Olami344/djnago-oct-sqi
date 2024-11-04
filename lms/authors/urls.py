from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "authors"

urlpatterns = [
    path("all-authors/", views.all_authors, name="all_authors"),
]
