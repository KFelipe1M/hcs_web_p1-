from django.contrib import admin
from django.urls import path, include

# site urls #
urlpatterns = [
    path("", include("encyclopedia.urls")),
    path('admin/', admin.site.urls),
    path("", include("encyclopedia.urls")),
]
