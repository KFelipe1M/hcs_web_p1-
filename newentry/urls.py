from django.urls import path
from encyclopedia import util
from . import views

app_name = "newentry"
urlpatterns = [
    path("",views.index, name="index"),
    path("newentrymaker", views.newentrymaker, name="newentrymaker"),
    path("<str:title>/", views.entry, name="entry"),
]