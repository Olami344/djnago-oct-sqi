from django.urls import path


from . import views

app_name = "library"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("book_list/", views.book_list, name="books"),
]