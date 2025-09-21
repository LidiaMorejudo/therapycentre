from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import BookASessionForm
from .models import BookASession

def booking(request):
    return render(request, 'booking/booking.html')

