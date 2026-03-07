from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def donate(request):
    return render(request, "donations/donate.html", {
        "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def success(request):
    return render(request, "donations/success.html")


def cancel(request):
    return render(request, "donations/cancel.html")


def create_checkout_session(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=[],
        success_url="http://example.com/success",
        cancel_url="http://example.com/cancel",
    )
    return JsonResponse({"id": session.id})
