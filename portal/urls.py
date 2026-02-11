from django.urls import path

from portal import views

urlpatterns = [
    path("", views.lookup, name="lookup"),
    path("lookup", views.submit_lookup, name="submit_lookup"),
    path("<str:order_number>", views.order_details, name="order_details"),
    path(
        "<str:order_number>/eligibility",
        views.recompute_eligibility,
        name="recompute_eligibility",
    ),
]
