from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import BookASession

class BookASessionForm(forms.ModelForm):
    """
    Form for creating and validating session bookings.
    This form is based on the `BookASession` model and provides custom validation
    for the booking date, time, and availability of sessions.
    Contains fields for:
        firstname (str) - first name of the person making the booking.
        lastname (str) - last name of the person making the booking.
        email (EmailField) - email address of the person making the booking.
        students (int) - number of students (between 1 and 10).
        date (DateField) - date of the booking.
        time (str) - time of the booking, chosen from predefined options.
        message (str) - optional message from the person making the booking.
    """
    policy_check = forms.BooleanField(
        required=True,
        label="I have read and agree to the Booking Policy",
        error_messages={'required': 'You must agree to the booking policy to proceed.'}
    )

    class Meta:
        model = BookASession
        fields = [
            'firstname', 'lastname', 'email', 'students',
            'date', 'time', 'message'
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'date_picker', 'type': 'date'}),
            'time': forms.Select(choices=BookASession.TIMESLOT_CHOICES, attrs={
                'class': 'form-control', 'id': 'time_picker'}),
            'students': forms.NumberInput(attrs={
                'class': 'form-control', 'min': '1', 'max': '10'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4}),
        }

    def clean_date(self):
        """
        Validates the booking date.
        Ensures that the booking date is not in the past and not more than
        30 days in the future.
        Raises ValidationError if the date is in the past or more 
        than 30 days ahead.
        """
        date = self.cleaned_data['date']
        today = timezone.now().date()
        if date < today:
            raise ValidationError("You cannot book a session in the past.")
        if date > today + timezone.timedelta(days=30):
            raise ValidationError(
                "You cannot book more than 30 days in advance.")
        return date

    def clean_time(self):
        """
        Validates the booking time.
        Ensures that the time selected is not in the past if the booking
        is for the current day.
        Raises ValidationError if the time is earlier 
        than current time for todays bookings.
        """
        date = self.cleaned_data.get('date')
        time = self.cleaned_data['time']
        now = timezone.now()
        current_time = now.strftime("%H:%M")

        if date == now.date() and time < current_time:
            raise ValidationError("You cannot book a session in the past.")
        return time

    def clean(self):
        """
        Performs full form validation, including checking seat availability.
        Combines the date, time, and number of students to check if there are available
        seats for chosen time slot.
        Raises ValidationError if there are no available seats.
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        students = cleaned_data.get('students')

        if date and time and students:
            bookings_at_time = BookASession.objects.bookings_for_time(date, time)
            total_seats = sum(booking.students for booking in bookings_at_time)
            if total_seats + students > 30:
                raise ValidationError(
                    "No available spaces in this session.")

        return cleaned_data