from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('findus/', views.findus, name='findus'),
    path('sessions/', views.sessions, name='sessions'),
]

