from django.urls import path
from . import views

app_name = "donations"

urlpatterns = [
    path("", views.donate, name="donate"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("create-checkout-session/", views.create_checkout_session, name="create_checkout_session"),
]