from django.urls import path
from encyclopedia import util
from . import views
from django.urls import path
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