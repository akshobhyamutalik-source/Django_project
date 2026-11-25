from django.urls import path
from . import views
from enquiries.views import contact_view

# URL patterns matching reference site https://puppy.instabizweb.com/
urlpatterns = [
    path('', views.home, name='home'),
    path('happy-families/', views.happy_families, name='happy_families'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('faq/', views.faq, name='faq'),
    path('contact/', contact_view, name='contact'),
]
