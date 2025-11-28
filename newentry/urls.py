from django.urls import path
from encyclopedia import util
from . import views

app_name = "newentry"

urlpatterns = [
    path("newentrymaker/", views.newentrymaker, name="newentrymaker"),
]