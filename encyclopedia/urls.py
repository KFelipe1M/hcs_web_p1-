from django.urls import path, include
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("newentrymaker/", views.newentrymaker, name="newentrymaker"),
    path("edit/<str:entry>/", views.edit, name="edit"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("random/", views.random, name="random"),

]