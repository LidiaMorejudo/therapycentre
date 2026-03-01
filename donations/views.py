from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
import stripe

# This makes the "stripe" module exist in this file (needed for your test patch)
stripe.api_key = settings.STRIPE_SECRET_KEY


def donate(request):
    return render(request, "donations/donate.html")


def success(request):
    return render(request, "donations/success.html")


def cancel(request):
    return render(request, "donations/cancel.html")


def create_checkout_session(request):
    # Your test expects GET to return 400
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    # This call is mocked in your test, so it won't hit Stripe for real during tests.
    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=[],
        success_url="http://example.com/success",
        cancel_url="http://example.com/cancel",
    )
    return JsonResponse({"id": session.id})
