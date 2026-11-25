from django.urls import path
from . import views

# URL patterns for puppies app
urlpatterns = [
    # List of all puppies: /puppies/
    path('', views.puppies, name='puppies'),

    # Detail page for a specific puppy: /puppies/1/
    path('<int:id>/', views.puppy_details, name='puppy_details'),
]
