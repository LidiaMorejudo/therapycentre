from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_session, name='booking'),  # main booking page
    path('my-bookings/', views.booking_list, name='booking_list'),  # list of user's bookings

    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('edit/confirmation/', views.edit_booking_confirmation, name='edit_booking_confirmation'),

    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('delete/confirmation/', views.delete_booking_confirmation, name='delete_booking_confirmation'),
]
