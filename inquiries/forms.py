from django import forms
from .models import Inquiries


class InquiriesForm(forms.ModelForm):
    """
    Form for creating and sending inquiries to the therapy centre.
    Connected to the admin panel for management.
    Contains fields for:
        subject (str) - subject of the inquiry.
        name (str) - name of the person submitting the inquiry.
        email (EmailField) - contact email of the person.
        message (str) - the inquiry content.
    """
    class Meta:
        model = Inquiries
        fields = ('subject', 'name', 'email', 'message')
