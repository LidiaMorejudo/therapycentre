from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    """
    Form for creating and sending enquiries to the therapy centre.
    Connected to the admin panel for management.
    Contains fields for:
        subject (str) - subject of the enquiry.
        name (str) - name of the person submitting the enquiry.
        email (EmailField) - contact email of the person.
        message (str) - the enquiry content.
    """
    class Meta:
        model = Enquiry
        fields = ('subject', 'name', 'email', 'message')
