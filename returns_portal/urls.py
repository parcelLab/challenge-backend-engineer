from django.urls import include, path

urlpatterns = [
    path("returns/", include("portal.urls")),
]
