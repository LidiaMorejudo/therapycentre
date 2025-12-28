from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def findus(request):
    return render(request, 'core/findus.html')


def sessions(request):
    return render(request, 'core/sessions.html')


def booking_view(request):
    return render(request, 'core/booking.html')
