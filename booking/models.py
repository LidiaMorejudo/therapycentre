from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


class BookingManager(models.Manager):
    """
    Custom manager for the BookATable model,
    providing methods for fetching bookings.
    """
    def todays_bookings(self):
        # Returns all bookings for the current date.
        return self.filter(date=timezone.now().date())

    def bookings_by_user(self, user):
        # Returns all bookings made by specified user.
        return self.filter(user=user)

    def bookings_for_time(self, date, time):
        # Return bookings made for a specific date and time slot.
        return self.filter(date=date, time=time)


class BookASession(models.Model):
    """
    Model representing a session booking made by a site user.
    Contains fields for:
        user (ForeignKey) - user who made the booking (nullable).
        firstname (CharField) - first name of the person who booked.
        lastname (CharField) - last name of the person who booked.
        email (EmailField) - email address of the person who booked.
        date (DateField) - date of the booking.
        time (CharField) - time slot of the booking, chosen from
        pre-defined options.
        students (PositiveIntegerField) - number of students (1 to 8).
        message (TextField) - optional message from the person booking.
        read (BooleanField) - indicates whether the booking has been marked
        as read by admin.
    """
    TIMESLOT_CHOICES = [
        ("15:00", "3 PM"),
        ("16:00", "4 PM"),
        ("17:00", "5 PM"),
        ("18:00", "6 PM"),
        ("19:00", "7 PM"),
        ("20:00", "8 PM"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIMESLOT_CHOICES)
    students = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)], default=1)
    message = models.TextField(blank=True, null=True)
    read = models.BooleanField(default=False)

    objects = BookingManager()

    def __str__(self):
        """
        String repres. of the booking object.
        Returns a string indicating booking:s last name, date and time.
        """
        return f"Booking made by {self.lastname} on {self.date} at {self.time}"

    def clean(self):
        """
        Validation logic for ensuring the booking is valid.
        Raises ValidationError ff the booking date or time is in the past,
        or if there are no available tables.
        """
        # Get current date and time
        now = timezone.now()
        current_date = now.date()
        current_time = now.strftime("%H:%M")

        # Check if date or time is None
        if self.date is None or self.time is None:
            raise ValidationError("Correct date and time must be provided.")

        # Prevent booking in the past
        if self.date < current_date:
            raise ValidationError("You cannot book a table in the past.")
        elif self.date == current_date and self.time < current_time:
            raise ValidationError("You cannot book a table in the past.")

        # Verify that bookings are fetched correctly
        bookings_at_time = BookASession.objects.bookings_for_time(
            self.date, self.time)

        # Calculate total spaces
        total_spaces = sum(booking.students for booking in bookings_at_time)

        if total_spaces + self.students > 30:
            raise ValidationError("No available spaces for this time slot.")


    def save(self, *args, **kwargs):
        """
        Override save method to include custom validation.
        """
        self.clean()  # Perform the validation check
        super().save(*args, **kwargs)


    class Meta:
        """
        Meta options for the BookASession model.
        Attributes: verbose_name (str), verbose_name_plural (str),
        ordering (list), constraints (list)
        """
        verbose_name = "Session Booking"
        verbose_name_plural = "Session Bookings"
        ordering = ['-date', '-time']
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'time', 'user'],
                name='unique_booking_per_user_per_time')
    ]


# Create your models here.
