from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.hello, name="intro"),
    path("myself/", views.myself, name="about_me")
]