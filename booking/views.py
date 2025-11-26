from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import BookASessionForm
from .models import BookASession


def book_session(request):
    """
    Handles creation of a new session booking.
    If POST: save booking, assign user if logged in, redirect to user's bookings.
    If GET: show empty booking form.
    """
    if request.method == "POST":
        booking_form = BookASessionForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            messages.success(request, "Booking successfully created!")
            return redirect('my_bookings')
        else:
            messages.error(
                request,
                "There was an error with your reservation request. Please check the form and try again."
            )
    else:
        booking_form = BookASessionForm()

    return render(request, 'booking/booking.html', {'booking_form': booking_form})


@login_required
def my_bookings(request):
    """
    Show bookings for the logged-in user.
    """
    bookings = BookASession.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'registration/mybookings.html', {'bookings': bookings})


@login_required
def edit_booking(request, pk):
    """
    Edit an existing booking for the logged-in user.
    """
    booking = get_object_or_404(BookASession, pk=pk, user=request.user)

    if request.method == "POST":
        form = BookASessionForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking successfully updated!")
            return redirect('my_bookings')
        else:
            messages.error(request, "There was an error updating your booking.")
    else:
        form = BookASessionForm(instance=booking)

    return render(request, 'registration/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, pk):
    """
    Delete an existing booking for the logged-in user.
    """
    booking = get_object_or_404(BookASession, pk=pk, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking successfully deleted!")
        return redirect('my_bookings')

    return render(request, 'registration/delete_booking.html', {'booking': booking})


def signup(request):
    """
    User sign-up view.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with sign-up. Please check the form.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
