from django.urls import path
from . import views

# URL patterns for enquiries app
urlpatterns = [
    path('', views.contact_view, name='enquiry'),
]
