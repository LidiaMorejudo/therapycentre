from django.urls import path
from . import views

urlpatterns = [
    # Booking
    path('', views.book_session, name='booking'),  # Create a booking
    path('list/', views.booking_list, name='booking_list'),  # List of bookings
    
    path('edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),  # Edit booking
    path('delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),  # Delete booking

    # User account / registration
    path('signup/', views.signup, name='signup'),  # User registration
]

