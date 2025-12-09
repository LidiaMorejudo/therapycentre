from django.contrib import admin
from .models import Inquiries

@admin.register(Inquiries)
class InquiriesAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "read")
    list_filter = ("read",)
    search_fields = ("name", "email", "subject")
