from django.contrib import admin
from .models import Enquiry

# Custom admin view for customer enquiries
class EnquiryAdmin(admin.ModelAdmin):
    # Columns displayed in the enquiries list
    list_display = ('name', 'email', 'phone', 'puppy', 'is_contacted', 'created_at')

    # Filter sidebar options
    list_filter = ('is_contacted', 'created_at', 'puppy')

    # Search bar fields
    search_fields = ('name', 'email', 'phone', 'message')

    # Allow admin to quickly toggle 'is_contacted' directly from the list table
    list_editable = ('is_contacted',)

    # Make the creation timestamp read-only
    readonly_fields = ('created_at',)

    # Number of enquiries shown per page
    list_per_page = 15

admin.site.register(Enquiry, EnquiryAdmin)
