from django.contrib import admin
from .models import BookASession

@admin.register(BookASession)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'firstname', 'lastname', 'email',
        'date', 'time', 'students', 'read', 'user'
    )
    list_filter = ('date', 'time', 'read')
    search_fields = ('firstname', 'lastname', 'email')
