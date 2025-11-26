from django.urls import path
from . import views

urlpatterns = [
    # Booking
    path('', views.book_session, name='booking'),  # Create a booking
    path('list/', views.booking_list, name='booking_list'),  # List of bookings (admin or user-specific)
    
    path('edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),  # Edit booking
    path('edit/confirmation/', views.booking_edit_confirmation, name='booking_edit_confirmation'),  # Edit confirmation
    
    path('delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),  # Delete booking
    path('delete/confirmation/', views.booking_delete_confirmation, name='booking_delete_confirmation'),  # Delete confirmation

    # User account / registration
    path('signup/', views.signup, name='signup'),  # User registration
    path('my-bookings/', views.my_bookings, name='my_bookings'),  # User's bookings
    path('edit-booking/<int:pk>/', views.edit_booking, name='edit_booking'),  # User edits their own booking
]

