from django.urls import path
from . import views

urlpatterns = [
    path('enquiries/', views.inquiries_view, name='inquiries_form'),
]
