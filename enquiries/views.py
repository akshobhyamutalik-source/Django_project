from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm
from puppies.models import Puppy

# View function to handle customer contact and puppy enquiries
def contact_view(request):
    """
    Handles displaying and submitting the enquiry/contact form.
    Supports pre-filling the puppy dropdown if '?puppy_id=...' is passed.
    """
    # Check if a specific puppy was selected from the puppy details page
    puppy_id = request.GET.get('puppy_id')
    initial_data = {}

    if puppy_id:
        try:
            selected_puppy = Puppy.objects.get(id=puppy_id)
            initial_data['puppy'] = selected_puppy
        except Puppy.DoesNotExist:
            pass

    # When user clicks the Submit button (POST request)
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        # Check if all required fields are filled out correctly
        if form.is_valid():
            # Save the new enquiry into SQLite database
            form.save()
            # Add a green success alert message
            messages.success(request, "🎉 Thank you! Your enquiry has been received successfully. Our puppy care team will call or email you soon!")
            return redirect('contact')
    else:
        # Normal GET request: create a blank (or pre-filled) form
        form = EnquiryForm(initial=initial_data)

    return render(request, 'contact.html', {
        'form': form
    })
