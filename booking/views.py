from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import BookASessionForm
from .models import BookASession


def book_session(request):
    """
    Handles creation of a new session booking.
    If POST: save booking, assign user, redirect to my bookings.
    If GET: show empty booking form.
    """
    if request.method == "POST":
        booking_form = BookASessionForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            return redirect('booking_list')  # or 'my_bookings', depending on your setup
        else:
            messages.error(
                request,
                "There was an error with your reservation request. "
                "Please check the form and try again."
            )
    else:
        booking_form = BookASessionForm()

    return render(request, 'booking/booking.html', {'booking_form': booking_form})


@login_required
def booking_list(request):
    """
    Shows all bookings made by the logged-in user.
    """
    bookings = BookASession.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


@login_required
def booking_edit(request, booking_id):
    """
    Edit a user’s existing booking.
    """
    booking = get_object_or_404(BookASession, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookASessionForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        messages.error(request, "There was an error updating your booking.")
    else:
        form = BookASessionForm(instance=booking)

    return render(request, 'booking/booking_edit.html', {'form': form, 'booking': booking})


@login_required
def booking_delete(request, booking_id):
    """
    Delete a user’s existing booking.
    """
    booking = get_object_or_404(BookASession, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')

    return render(request, 'booking/booking_delete.html', {'booking': booking})


def signup(request):
    """
    User sign-up view.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
