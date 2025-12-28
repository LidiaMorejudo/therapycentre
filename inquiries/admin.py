from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "read")
    list_filter = ("read",)
    search_fields = ("name", "email", "subject")
