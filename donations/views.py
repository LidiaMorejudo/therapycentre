from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
from django.urls import reverse
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

# Allowed donation amounts in pence
ALLOWED_AMOUNTS = {500, 1000, 2000}  # £5, £10, £20


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

    try:
        body = json.loads(request.body or "{}")
        amount = int(body.get("amount", 500))
    except Exception:
        amount = 500

    if amount not in ALLOWED_AMOUNTS:
        return JsonResponse({"error": "Invalid donation amount."}, status=400)

    success_url = request.build_absolute_uri(reverse("donations:success"))
    cancel_url = request.build_absolute_uri(reverse("donations:cancel"))

    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "gbp",
                    "product_data": {"name": "Donation"},
                    "unit_amount": amount,
                },
                "quantity": 1,
            }],
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return JsonResponse({"id": session.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
