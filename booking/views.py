from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import BookASessionForm
from .models import BookASession
from django.contrib.auth.forms import UserCreationForm


def book_session(request):
    """
    Handles the creation of a new session booking.
    If POST, validates the form data and creates a booking associated
    with the authenticated user (if logged in).
    Redirects to 'my_bookings' on success.
    """
    if request.method == "POST":
        booking_form = BookASessionForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            return redirect('my_bookings')
        else:
            messages.error(
                request,
                "There was an error with your reservation request. "
                "Please check the form and try again."
            )
    else:
        booking_form = BookAS_
