from django.shortcuts import render, get_object_or_404
from .models import Puppy

# View function to display all puppies (matching TeddyPups catalog)
def puppies(request):
    """
    Fetches puppies from the database.
    Splits them into 'Available' and 'Already gone home' matching TeddyPups.
    Supports search by breed name.
    """
    search_query = request.GET.get('search')

    if search_query:
        # Search across both available and adopted pups
        available_puppies = Puppy.objects.filter(is_available=True, breed__icontains=search_query)
        gone_home_puppies = Puppy.objects.filter(is_available=False, breed__icontains=search_query)
    else:
        available_puppies = Puppy.objects.filter(is_available=True)
        gone_home_puppies = Puppy.objects.filter(is_available=False)

    return render(request, 'puppies.html', {
        'puppies': available_puppies,
        'gone_home_puppies': gone_home_puppies,
        'search_query': search_query
    })


# View function for individual puppy details
def puppy_details(request, id):
    """
    Fetches single puppy by ID and 3 recommendations.
    """
    puppy = get_object_or_404(Puppy, id=id)
    other_puppies = Puppy.objects.exclude(id=id)[:3]

    return render(request, 'puppy_details.html', {
        'puppy': puppy,
        'other_puppies': other_puppies
    })
