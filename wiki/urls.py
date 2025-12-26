from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("encyclopedia.urls")),
    path('admin/', admin.site.urls),
    path("", include("encyclopedia.urls")),
]
