from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_session, name='booking'),
    path('list/', views.booking_list, name='booking_list'),

    path('edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('edit/confirmation/', views.booking_edit_confirmation, name='booking_edit_confirmation'),

    path('delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
    path('delete/confirmation/', views.booking_delete_confirmation, name='booking_delete_confirmation'),

    # User system
    path('signup/', views.signup, name='signup'),
]

