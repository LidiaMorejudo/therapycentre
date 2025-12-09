from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InquiriesForm  # your form

def inquiries_view(request):
    """
    Handles the inquiries form for users to send messages.
    If POST and form is valid, saves the message and redirects
    with ?success=true to trigger a confirmation modal.
    """
    inquiries_form = InquiriesForm()

    if request.method == "POST":
        inquiries_form = InquiriesForm(data=request.POST)
        if inquiries_form.is_valid():
            inquiries_form.save()
            return redirect(f"{reverse('inquiries')}?success=true")  # use URL name

    return render(
        request,
        'inquiries/inquiries.html',
        {'inquiries_form': inquiries_form},
    )
