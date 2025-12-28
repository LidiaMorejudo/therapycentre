import logging
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import BookASession

logger = logging.getLogger(__name__)


@receiver(user_signed_up)
def handle_user_signed_up(sender, request, user, **kwargs):
    email = user.email
    logger.info(f"User signed up with email: {email}")

    # Find all bookings with the same email where the user field is empty
    bookings = BookASession.objects.filter(email=email, user__isnull=True)
    logger.info(f"Found {bookings.count()} bookings for this email")

    if bookings.exists():
        # Link these bookings to the newly registered user
        bookings.update(user=user)
        logger.info(f"Updated bookings for user: {user}")
    else:
        logger.info(f"No bookings found for email: {email}")
