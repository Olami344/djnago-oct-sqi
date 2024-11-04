from django.urls import path, include

app_name = "pages"


from . import views
urlpatterns =[
    # path("/", views.bakerry, name="bakerry"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
]