from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_session, name='booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('booking/edit/confirmation/', views.booking_edit_confirmation, name='booking_edit_confirmation'),
    path('booking/delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
    path('booking/delete/confirmation/', views.booking_delete_confirmation, name='booking_delete_confirmation'),
]
