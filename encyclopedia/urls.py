from django.urls import path, include
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"), # index url path #
    path("search/", views.search, name="search"), # search function page url path #
    path("newentrymaker/", views.newentrymaker, name="newentrymaker"), # entry maker page url path #
    path("edit/<str:entry>/", views.edit, name="edit"), # edit function path #
    path("wiki/<str:title>/", views.entry, name="entry"), # entry visualization url path #
    path("random/", views.random, name="random"), # random page function #

]