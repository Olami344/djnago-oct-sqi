from django.urls import path
from . import views

urlpatterns=[
    path("welcome/", views.home_page, name="welcome")
]