from django.contrib import admin
from .models import BookASession

@admin.register(BookASession)
class BookASessionAdmin(admin.ModelAdmin):
    list_display = (
        'firstname', 'lastname', 'email',
        'date', 'time', 'students', 'read', 'user'
    )
    list_filter = ('date', 'time', 'read')
    search_fields = ('firstname', 'lastname', 'email')
    # Ordering by newest date and time first
    ordering = ('-date', '-time')

    # Fields to display in the add/edit form
    fields = (
        'firstname', 'lastname', 'email',
        'date', 'time', 'students', 'message', 'read', 'user'
    )
