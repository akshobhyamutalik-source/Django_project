from django.shortcuts import render
from puppies.models import Puppy

# 1. Home page view (TeddyPups luxury homepage)
def home(request):
    """
    Renders TeddyPups Dubai homepage with featured teacup puppies.
    """
    featured_puppies = Puppy.objects.filter(is_available=True)[:3]
    return render(request, 'home.html', {
        'puppies': featured_puppies
    })


# 2. Happy Families view (matching /happy-families)
def happy_families(request):
    """
    Renders Happy Families customer gallery and stories across Dubai & UAE.
    """
    gone_home_puppies = Puppy.objects.filter(is_available=False)
    return render(request, 'happy_families.html', {
        'gone_home_puppies': gone_home_puppies
    })


# 3. How It Works view (matching /how-it-works)
def how_it_works(request):
    """
    Renders How It Works: Two Ways Home, The Premium Puppy Promise, Delivery in Dubai.
    """
    return render(request, 'how_it_works.html')


# 4. FAQ view (matching /faq)
def faq(request):
    """
    Renders the exact 7 Questions & Answers from TeddyPups.
    """
    return render(request, 'faq.html')
