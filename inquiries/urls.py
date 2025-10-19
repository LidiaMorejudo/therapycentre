from django.urls import path
from . import views

urlpatterns = [
    path('', views.inquiries_view, name='inquiries'),
]
