from django.contrib import admin
from django.utils.html import format_html
from .models import Puppy

# Custom admin view for Puppy model
class PuppyAdmin(admin.ModelAdmin):
    # Method to render a small image preview in the admin table
    def photo_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "No Photo"

    photo_preview.short_description = "Photo"

    # Columns displayed in the puppies list
    list_display = (
        'photo_preview', 
        'name', 
        'breed', 
        'age', 
        'gender', 
        'price', 
        'is_available', 
        'is_vaccinated',
        'created_at'
    )

    # Filter sidebar options
    list_filter = ('breed', 'gender', 'is_available', 'is_vaccinated')

    # Search bar fields
    search_fields = ('name', 'breed', 'description')

    # Fields that can be edited directly from the list table
    list_editable = ('price', 'is_available', 'is_vaccinated')

    # Number of puppies shown per page
    list_per_page = 10

admin.site.register(Puppy, PuppyAdmin)
