from django.urls import path
from . import views

urlpatterns = [
    # Booking
    path('', views.book_session, name='booking'),  # Create a booking
    path('my-bookings/', views.my_bookings, name='my_bookings'),  # User's bookings
    path('edit-booking/<int:pk>/', views.edit_booking, name='edit_booking'),  # Edit booking
    path('delete-booking/<int:pk>/', views.delete_booking, name='delete_booking'),  # Delete booking

    # User account / registration
    path('signup/', views.signup, name='signup'),  # User registration
]

