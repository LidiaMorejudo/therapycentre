from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookASessionForm
from .models import BookASession


def book_session(request):
    """
    Handles creation of a new session booking.
    If POST: save booking, assign user if logged in, redirect with success query for modal.
    If GET: show empty booking form.
    """
    if request.method == "POST":
        booking_form = BookASessionForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            else:
                booking.user = None
            booking.save()
            # Redirect to same page with success query so modal can show
            return redirect('/booking/?success=true')
        else:
            messages.error(
                request,
                "There was an error with your booking. Please check the form and try again."
            )
    else:
        booking_form = BookASessionForm()

    return render(request, 'booking/booking.html', {'booking_form': booking_form})


@login_required
def booking_list(request):
    """
    Show bookings for the logged-in user.
    """
    bookings = BookASession.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """
    Edit an existing booking.
    """
    booking = get_object_or_404(BookASession, pk=booking_id, user=request.user)

    if request.method == "POST":
        form = BookASessionForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('edit_booking_confirmation')
        else:
            messages.error(request, "There was an error updating your booking.")
    else:
        form = BookASessionForm(instance=booking)

    return render(request, 'booking/edit_booking.html', {'form': form, 'booking': booking})


@login_required
def edit_booking_confirmation(request):
    """
    Confirmation page after editing a booking.
    """
    return render(request, 'booking/edit_booking_confirmation.html')


@login_required
def delete_booking(request, booking_id):
    """
    Delete an existing booking.
    """
    booking = get_object_or_404(BookASession, pk=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect('delete_booking_confirmation')

    return render(request, 'booking/delete_booking.html', {'booking': booking})


@login_required
def delete_booking_confirmation(request):
    """
    Confirmation page after deleting a booking.
    """
    return render(request, 'booking/delete_booking_confirmation.html')
