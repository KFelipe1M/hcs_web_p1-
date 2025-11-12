from django.contrib import admin
from encyclopedia import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("encyclopedia.urls")),
    path('newentry/', include("newentry.urls"))
]
