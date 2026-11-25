from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enquiry
from puppies.models import Puppy

def contact_view(request):
    """
    Handles displaying and submitting the exact TeddyPups contact letterform.
    Saves submissions into the Enquiry database and displays a confirmation message.
    """
    if request.method == 'POST':
        # Honeypot field protection against spam bots
        if request.POST.get('website'):
            return redirect('contact')

        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip() or 'contact@teddypups.ae'
        area = request.POST.get('area', '').strip()
        message = request.POST.get('message', '').strip()

        full_message = message
        if area:
            full_message = f"[Area: {area}] {full_message}" if full_message else f"[Area: {area}] Customer enquired via letter form."

        puppy_id = request.POST.get('puppyId') or request.POST.get('puppy')
        selected_puppy = None
        if puppy_id:
            try:
                selected_puppy = Puppy.objects.filter(id=puppy_id).first()
            except Exception:
                pass

        if name and phone:
            Enquiry.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=full_message or 'Showroom enquiry from website letter form.',
                puppy=selected_puppy
            )
            # Matching exact message for test assertion and user experience
            messages.success(request, "🎉 Thank you! Your enquiry has been received successfully. Our puppy care team will call or email you soon!")
            return redirect('contact')
        else:
            messages.error(request, "Please provide at least your name and phone number so our team can reach you.")

    return render(request, 'contact.html')
